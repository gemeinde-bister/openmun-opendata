"""API for Swiss official street directory (Amtliches Strassenverzeichnis)."""

from typing import Iterator, List, Literal, Optional
from openmun_opendata.geo.base import BaseGeoAPI
from openmun_opendata.geo.models.streets import StreetV1


class StreetsAPI(BaseGeoAPI):
    """API for accessing Swiss official street directory.

    This API provides access to the official Swiss street directory
    (Amtliches Strassenverzeichnis) from swisstopo. Data is fetched from
    data.geo.admin.ch via STAC API and can fall back to cached data.

    Data Source:
        ch.swisstopo.amtliches-strassenverzeichnis
        Update Frequency: Regular updates

    Model Versions:
        v1: Current stable version (default)

    Note:
        This dataset contains 220,000+ streets. Use streaming methods
        (iter_all, iter_by_municipality) for memory efficiency.

    Examples:
        >>> # Stream streets to database (recommended)
        >>> api = StreetsAPI()
        >>> for street in api.iter_all():
        ...     db.insert(street)

        >>> # With fallback to cached data
        >>> api = StreetsAPI(fallback_allowed=True)

        >>> # Explicit version pinning
        >>> api = StreetsAPI(model_version='v1')

        >>> # Filter by municipality (streaming)
        >>> api = StreetsAPI(fallback_allowed=True)
        >>> for street in api.iter_by_municipality(261):
        ...     process(street)

    Attributes:
        model_version: Model version to use ('v1' currently)
        fallback_allowed: Whether to use cached data if remote fetch fails
    """

    def __init__(
        self,
        model_version: Literal['v1'] = 'v1',
        fallback_allowed: bool = False,
        **kwargs
    ):
        """Initialize Streets API.

        Args:
            model_version: Model version to use (only 'v1' currently available)
            fallback_allowed: Allow using cached data if remote fetch fails
            **kwargs: Additional arguments passed to BaseGeoAPI
        """
        super().__init__(fallback_allowed=fallback_allowed, **kwargs)
        self.model_version = model_version

        # Setup version-specific configuration
        self._setup_version()

    def _setup_version(self):
        """Setup version-specific dataset parameters."""
        if self.model_version == 'v1':
            # V1 configuration
            self.collection_id = "ch.swisstopo.amtliches-strassenverzeichnis"
            self.item_id = "amtliches-strassenverzeichnis_ch"
            self.zip_filename = "amtliches-strassenverzeichnis_ch_2056.csv.zip"
            self.csv_filename = "amtliches-strassenverzeichnis_ch_2056.csv"
            self.csv_delimiter = ';'
            self._parse_row_func = self._parse_row_v1
        else:
            from openmun_opendata.geo.base import GeoAPIError
            raise GeoAPIError(f"Unsupported model version: {self.model_version}")

    def _fetch_remote(self) -> str:
        """Fetch streets CSV from remote STAC API.

        Returns:
            CSV content as string

        Raises:
            RemoteFetchError: If fetch fails
        """
        from openmun_opendata.geo.base import RemoteFetchError

        # Get STAC items
        items_data = self._get_stac_collection_items(self.collection_id)

        # Find Switzerland item
        ch_item = None
        for feature in items_data.get('features', []):
            if feature['id'] == self.item_id:
                ch_item = feature
                break

        if not ch_item:
            raise RemoteFetchError(
                f"Could not find item {self.item_id} in STAC collection"
            )

        # Get CSV asset
        assets = ch_item.get('assets', {})
        csv_asset = assets.get(self.zip_filename)

        if not csv_asset:
            raise RemoteFetchError(f"Could not find CSV asset {self.zip_filename}")

        # Download ZIP
        url = csv_asset['href']
        cache_path = self.cache_dir / self.zip_filename
        zip_content = self._download_file(url, destination=cache_path)

        # Extract CSV (it's directly in the ZIP, not in subdirectory)
        return self._extract_csv_from_zip(zip_content)

    def _fetch_fallback(self) -> str:
        """Get streets CSV from local cache.

        Returns:
            CSV content as string

        Raises:
            NoFallbackDataError: If local data not found
        """
        # Try ZIP first
        try:
            return self._read_local_csv(self.zip_filename, from_zip=True)
        except Exception:
            # Try extracted CSV
            return self._read_local_csv(self.csv_filename, from_zip=False)

    def _get_csv_content(self) -> str:
        """Get CSV content either from remote or fallback.

        Returns:
            CSV content as string
        """
        return self._fetch_or_fallback(
            fetch_func=self._fetch_remote,
            fallback_func=self._fetch_fallback,
            error_context="streets"
        )

    def _parse_row_v1(self, row: dict) -> StreetV1:
        """Parse CSV row to StreetV1 model.

        Args:
            row: Dictionary from CSV reader

        Returns:
            StreetV1 instance
        """
        return StreetV1(
            esid=row['STR_ESID'],
            name=row['STN_LABEL'],
            postal_codes=row['ZIP_LABEL'],
            municipality_bfs=int(row['COM_FOSNR']),
            municipality_name=row['COM_NAME'],
            canton_code=row['COM_CANTON'],
            street_type=row['STR_TYPE'],
            status=row['STR_STATUS'],
            is_official=row['STR_OFFICIAL'],
            modified_date=row['STR_MODIFIED'],
            easting=float(row['STR_EASTING']),
            northing=float(row['STR_NORTHING']),
            parent_esid=row.get('STR_PARENT') or None,
            children_esids=row.get('STR_CHILDREN') or None
        )

    def iter_all(self) -> Iterator[StreetV1]:
        """Iterate over all streets.

        This is the recommended method for processing streets as it streams
        data without loading 220,000+ streets into memory.

        Yields:
            StreetV1 instances

        Examples:
            >>> api = StreetsAPI()
            >>> count = 0
            >>> for street in api.iter_all():
            ...     count += 1
            ...     if count % 10000 == 0:
            ...         print(f"Processed {count:,} streets...")
            Processed 10,000 streets...
            Processed 20,000 streets...
            ...

            >>> # Stream to database
            >>> api = StreetsAPI(fallback_allowed=True)
            >>> for street in api.iter_all():
            ...     db.insert(street)
        """
        csv_content = self._get_csv_content()

        for row in self._parse_csv(csv_content, delimiter=self.csv_delimiter):
            yield self._parse_row_func(row)

    def get_all(self) -> List[StreetV1]:
        """Get all streets as a list.

        WARNING: This loads all 220,000+ streets into memory (~50MB+).
        Prefer iter_all() for memory-efficient processing.

        Returns:
            List of StreetV1 instances

        Examples:
            >>> api = StreetsAPI(fallback_allowed=True)
            >>> streets = api.get_all()  # Takes time and memory
            >>> len(streets)
            224560
        """
        return list(self.iter_all())

    def get_by_esid(self, esid: str) -> Optional[StreetV1]:
        """Get a street by its ESID (Federal Street Identifier).

        Note: This iterates through all streets until found. For batch
        lookups, consider loading into a database with ESID index.

        Args:
            esid: The ESID to search for (e.g., '10194929')

        Returns:
            StreetV1 instance or None if not found

        Examples:
            >>> api = StreetsAPI(fallback_allowed=True)
            >>> street = api.get_by_esid('10194929')
            >>> if street:
            ...     print(street.name)
            Untere Kirchenholzstrasse
        """
        esid = esid.strip()
        for street in self.iter_all():
            if street.esid == esid:
                return street
        return None

    def get_by_municipality(self, bfs_number: int) -> List[StreetV1]:
        """Get all streets in a specific municipality.

        Note: This loads all matching streets into memory. For large
        municipalities (e.g., Zürich with 2,500+ streets), prefer
        iter_by_municipality().

        Args:
            bfs_number: BFS municipality number (e.g., 261 for Zürich)

        Returns:
            List of matching StreetV1 instances

        Examples:
            >>> api = StreetsAPI(fallback_allowed=True)
            >>> streets = api.get_by_municipality(261)  # Zürich
            >>> len(streets)
            2519
            >>> streets[0].name
            'Brombeeriweg'
        """
        return [
            street for street in self.iter_all()
            if street.municipality_bfs == bfs_number
        ]

    def get_by_canton(self, canton_code: str) -> List[StreetV1]:
        """Get all streets in a specific canton.

        WARNING: This loads all canton streets into memory. For large cantons
        (e.g., ZH with 50,000+ streets), prefer iter_by_canton().

        Args:
            canton_code: Two-letter canton code (e.g., 'ZH', 'GE')

        Returns:
            List of matching StreetV1 instances

        Examples:
            >>> api = StreetsAPI(fallback_allowed=True)
            >>> streets = api.get_by_canton('GE')
            >>> len(streets)
            15000+
        """
        canton_code = canton_code.upper().strip()
        return [
            street for street in self.iter_all()
            if street.canton_code == canton_code
        ]

    def iter_by_municipality(self, bfs_number: int) -> Iterator[StreetV1]:
        """Iterate streets in a specific municipality (memory efficient).

        This is the recommended method for processing municipal streets.

        Args:
            bfs_number: BFS municipality number

        Yields:
            StreetV1 instances

        Examples:
            >>> api = StreetsAPI(fallback_allowed=True)
            >>> for street in api.iter_by_municipality(261):  # Zürich
            ...     db.insert(street)

            >>> # Count streets per municipality
            >>> count = sum(1 for _ in api.iter_by_municipality(261))
            >>> print(f"Zürich has {count:,} streets")
            Zürich has 2,519 streets
        """
        for street in self.iter_all():
            if street.municipality_bfs == bfs_number:
                yield street

    def iter_by_canton(self, canton_code: str) -> Iterator[StreetV1]:
        """Iterate streets in a specific canton (memory efficient).

        Args:
            canton_code: Two-letter canton code

        Yields:
            StreetV1 instances

        Examples:
            >>> api = StreetsAPI(fallback_allowed=True)
            >>> for street in api.iter_by_canton('ZH'):
            ...     process(street)
        """
        canton_code = canton_code.upper().strip()
        for street in self.iter_all():
            if street.canton_code == canton_code:
                yield street

    def iter_by_postal_code(self, postal_code: str) -> Iterator[StreetV1]:
        """Iterate streets associated with a specific postal code.

        Note: A street can be associated with multiple postal codes.

        Args:
            postal_code: 4-digit postal code (e.g., '8001')

        Yields:
            StreetV1 instances

        Examples:
            >>> api = StreetsAPI(fallback_allowed=True)
            >>> for street in api.iter_by_postal_code('8001'):
            ...     print(street.name)
        """
        postal_code = postal_code.strip()
        for street in self.iter_all():
            if postal_code in street.postal_code_list:
                yield street
