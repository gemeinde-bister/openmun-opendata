"""Base API class for Swiss geodata access."""

import csv
import json
import zipfile
from io import StringIO, BytesIO
from pathlib import Path
from typing import Optional, Dict, Any, Iterator, List
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


class GeoAPIError(Exception):
    """Base exception for geo API errors."""
    pass


class RemoteFetchError(GeoAPIError):
    """Error fetching data from remote API."""
    pass


class NoFallbackDataError(GeoAPIError):
    """No fallback data available and remote fetch failed."""
    pass


class BaseGeoAPI:
    """Base class for accessing Swiss geodata from data.geo.admin.ch.

    This class handles:
    - Fetching data from remote API
    - Caching to local sources directory
    - Fallback to local data when remote unavailable
    - CSV parsing from ZIP archives
    """

    def __init__(
        self,
        fallback_allowed: bool = False,
        cache_dir: Optional[Path] = None,
        sources_dir: Optional[Path] = None
    ):
        """Initialize geo API.

        Args:
            fallback_allowed: Allow using local cached data if remote fetch fails
            cache_dir: Directory to cache downloaded files (default: sources/swisstopo)
            sources_dir: Directory with pre-downloaded fallback data (default: sources/swisstopo)
        """
        self.fallback_allowed = fallback_allowed

        # Determine project root
        self.project_root = Path(__file__).parent.parent.parent

        # Set directories
        self.cache_dir = cache_dir or (self.project_root / "sources" / "swisstopo")
        self.sources_dir = sources_dir or (self.project_root / "sources" / "swisstopo")

        # API endpoints
        self.base_url = "https://data.geo.admin.ch"
        self.stac_api = f"{self.base_url}/api/stac/v0.9"

    def _download_file(self, url: str, destination: Optional[Path] = None) -> bytes:
        """Download a file from URL.

        Args:
            url: URL to download from
            destination: Optional path to save file to

        Returns:
            File contents as bytes

        Raises:
            RemoteFetchError: If download fails
        """
        try:
            request = Request(url, headers={'User-Agent': 'OpenMun-OpenData/1.0'})
            with urlopen(request, timeout=30) as response:
                if response.status != 200:
                    raise RemoteFetchError(f"HTTP {response.status}: {url}")

                content = response.read()

                # Save to destination if provided
                if destination:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    with open(destination, 'wb') as f:
                        f.write(content)

                return content

        except (HTTPError, URLError) as e:
            raise RemoteFetchError(f"Failed to download {url}: {e}")
        except Exception as e:
            raise RemoteFetchError(f"Unexpected error downloading {url}: {e}")

    def _get_stac_collection_items(self, collection_id: str) -> Dict[str, Any]:
        """Fetch STAC collection items from API.

        Args:
            collection_id: STAC collection identifier

        Returns:
            JSON response

        Raises:
            RemoteFetchError: If fetch fails
        """
        url = f"{self.stac_api}/collections/{collection_id}/items"

        try:
            request = Request(url, headers={'User-Agent': 'OpenMun-OpenData/1.0'})
            with urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            raise RemoteFetchError(f"Failed to fetch STAC items for {collection_id}: {e}")

    def _extract_csv_from_zip(self, zip_content: bytes, csv_filename: Optional[str] = None) -> str:
        """Extract CSV content from ZIP archive.

        Args:
            zip_content: ZIP file as bytes
            csv_filename: Specific CSV filename to extract (or None for first CSV)

        Returns:
            CSV content as string

        Raises:
            GeoAPIError: If extraction fails
        """
        try:
            with zipfile.ZipFile(BytesIO(zip_content)) as zf:
                # Find CSV file
                csv_files = [f for f in zf.namelist() if f.endswith('.csv')]

                if not csv_files:
                    raise GeoAPIError("No CSV file found in ZIP archive")

                # Use specific file or first one
                if csv_filename:
                    if csv_filename not in zf.namelist():
                        raise GeoAPIError(f"CSV file {csv_filename} not found in ZIP")
                    target_file = csv_filename
                else:
                    target_file = csv_files[0]

                # Extract and decode
                csv_bytes = zf.read(target_file)

                # Try UTF-8 first, then UTF-8 with BOM
                try:
                    return csv_bytes.decode('utf-8')
                except UnicodeDecodeError:
                    return csv_bytes.decode('utf-8-sig')

        except zipfile.BadZipFile as e:
            raise GeoAPIError(f"Invalid ZIP file: {e}")
        except Exception as e:
            raise GeoAPIError(f"Failed to extract CSV: {e}")

    def _read_local_csv(self, filename: str, from_zip: bool = True) -> str:
        """Read CSV from local sources directory.

        Args:
            filename: Name of the file (ZIP or CSV)
            from_zip: Whether to extract from ZIP

        Returns:
            CSV content as string

        Raises:
            NoFallbackDataError: If local file not found
        """
        if from_zip:
            zip_path = self.sources_dir / filename
            if not zip_path.exists():
                raise NoFallbackDataError(f"Fallback ZIP file not found: {zip_path}")

            try:
                with open(zip_path, 'rb') as f:
                    zip_content = f.read()
                return self._extract_csv_from_zip(zip_content)
            except Exception as e:
                raise NoFallbackDataError(f"Failed to read fallback ZIP: {e}")
        else:
            csv_path = self.sources_dir / filename
            if not csv_path.exists():
                raise NoFallbackDataError(f"Fallback CSV file not found: {csv_path}")

            try:
                with open(csv_path, 'r', encoding='utf-8-sig') as f:
                    return f.read()
            except Exception as e:
                raise NoFallbackDataError(f"Failed to read fallback CSV: {e}")

    def _parse_csv(
        self,
        csv_content: str,
        delimiter: str = ';',
        skip_bom: bool = True
    ) -> Iterator[Dict[str, str]]:
        """Parse CSV content into dictionaries.

        Args:
            csv_content: CSV content as string
            delimiter: CSV delimiter
            skip_bom: Skip UTF-8 BOM if present

        Yields:
            Dictionary for each row
        """
        # Remove BOM if present
        if skip_bom and csv_content.startswith('\ufeff'):
            csv_content = csv_content[1:]

        # Parse CSV
        reader = csv.DictReader(StringIO(csv_content), delimiter=delimiter)
        yield from reader

    def _fetch_or_fallback(
        self,
        fetch_func,
        fallback_func,
        error_context: str = "data"
    ):
        """Try to fetch data remotely, fall back to local if allowed.

        Args:
            fetch_func: Function to fetch remote data
            fallback_func: Function to get fallback data
            error_context: Description for error messages

        Returns:
            Result from fetch_func or fallback_func

        Raises:
            NoFallbackDataError: If both remote and fallback fail
        """
        try:
            return fetch_func()
        except RemoteFetchError as e:
            if not self.fallback_allowed:
                raise NoFallbackDataError(
                    f"Failed to fetch {error_context} from remote API and fallback not allowed. "
                    f"Use fallback_allowed=True to use cached data. Error: {e}"
                )

            try:
                return fallback_func()
            except NoFallbackDataError:
                raise NoFallbackDataError(
                    f"Failed to fetch {error_context} from remote API and no fallback data available. "
                    f"Original error: {e}"
                )
