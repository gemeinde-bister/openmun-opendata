"""API for Swiss postal codes and localities (Ortschaftenverzeichnis PLZ)."""

from typing import Iterator, List, Literal
from openmun_opendata.geo.base import BaseGeoAPI
from openmun_opendata.geo.models.postal_codes import PostalLocalityV1


class PostalCodesAPI(BaseGeoAPI):
    """API for accessing Swiss postal codes and localities.

    This API provides access to the official Swiss postal locality directory
    (Ortschaftenverzeichnis PLZ) from swisstopo. Data is fetched from
    data.geo.admin.ch and can fall back to cached data if unavailable.

    Data Source:
        ch.swisstopo-vd.ortschaftenverzeichnis_plz
        Update Frequency: Monthly

    Model Versions:
        v1: Current stable version (default)

    Examples:
        >>> # Default: fetch latest data, return V1 models
        >>> api = PostalCodesAPI()
        >>> for locality in api.iter_all():
        ...     db.insert(locality)

        >>> # With fallback to cached data
        >>> api = PostalCodesAPI(fallback_allowed=True)
        >>> localities = api.get_all()

        >>> # Explicit version pinning (for production stability)
        >>> api = PostalCodesAPI(model_version='v1')

        >>> # Filter by postal code
        >>> api = PostalCodesAPI(fallback_allowed=True)
        >>> zurich_localities = api.get_by_postal_code('8001')

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
        """Initialize Postal Codes API.

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
            self.dataset_url = (
                "https://data.geo.admin.ch/"
                "ch.swisstopo-vd.ortschaftenverzeichnis_plz/"
                "ortschaftenverzeichnis_plz/"
                "ortschaftenverzeichnis_plz_2056.csv.zip"
            )
            self.zip_filename = "ortschaftenverzeichnis_plz_2056.csv.zip"
            self.csv_path_in_zip = "AMTOVZ_CSV_LV95/AMTOVZ_CSV_LV95.csv"
            self.csv_delimiter = ';'
            self._parse_row_func = self._parse_row_v1
        else:
            from openmun_opendata.geo.base import GeoAPIError
            raise GeoAPIError(f"Unsupported model version: {self.model_version}")

    def _fetch_remote(self) -> str:
        """Fetch postal codes CSV from remote API.

        Returns:
            CSV content as string

        Raises:
            RemoteFetchError: If fetch fails
        """
        # Download ZIP
        cache_path = self.cache_dir / self.zip_filename
        zip_content = self._download_file(self.dataset_url, destination=cache_path)

        # Extract CSV
        return self._extract_csv_from_zip(zip_content, self.csv_path_in_zip)

    def _fetch_fallback(self) -> str:
        """Get postal codes CSV from local cache.

        Returns:
            CSV content as string

        Raises:
            NoFallbackDataError: If local data not found
        """
        return self._read_local_csv(self.zip_filename, from_zip=True)

    def _get_csv_content(self) -> str:
        """Get CSV content either from remote or fallback.

        Returns:
            CSV content as string
        """
        return self._fetch_or_fallback(
            fetch_func=self._fetch_remote,
            fallback_func=self._fetch_fallback,
            error_context="postal codes"
        )

    def _parse_row_v1(self, row: dict) -> PostalLocalityV1:
        """Parse CSV row to PostalLocalityV1 model.

        Args:
            row: Dictionary from CSV reader

        Returns:
            PostalLocalityV1 instance
        """
        return PostalLocalityV1(
            locality_name=row['Ortschaftsname'],
            postal_code=row['PLZ'],
            additional_digit=row['Zusatzziffer'],
            municipality_name=row['Gemeindename'],
            bfs_number=int(row['BFS-Nr']),
            canton_code=row['Kantonskürzel'],
            easting=float(row['E']),
            northing=float(row['N']),
            language=row['Sprache'],
            validity_date=row['Validity']
        )

    def iter_all(self) -> Iterator[PostalLocalityV1]:
        """Iterate over all postal localities.

        This is the recommended method for processing postal codes as it
        streams data without loading everything into memory.

        Yields:
            PostalLocalityV1 instances

        Examples:
            >>> api = PostalCodesAPI()
            >>> for locality in api.iter_all():
            ...     print(f"{locality.postal_code} {locality.locality_name}")
            8914 Aeugst am Albis
            8914 Aeugstertal
            ...

            >>> # Stream to database
            >>> api = PostalCodesAPI(fallback_allowed=True)
            >>> for locality in api.iter_all():
            ...     db.insert(locality)
        """
        csv_content = self._get_csv_content()

        for row in self._parse_csv(csv_content, delimiter=self.csv_delimiter):
            yield self._parse_row_func(row)

    def get_all(self) -> List[PostalLocalityV1]:
        """Get all postal localities as a list.

        Note: This loads all ~5,700 localities into memory. For large-scale
        processing, prefer iter_all() which streams data.

        Returns:
            List of PostalLocalityV1 instances

        Examples:
            >>> api = PostalCodesAPI(fallback_allowed=True)
            >>> localities = api.get_all()
            >>> len(localities)
            5754
            >>> localities[0].locality_name
            'Aeugst am Albis'
        """
        return list(self.iter_all())

    def get_by_postal_code(self, postal_code: str) -> List[PostalLocalityV1]:
        """Get all localities with a specific postal code.

        Multiple localities can share the same postal code (e.g., neighborhoods
        in a city).

        Args:
            postal_code: 4-digit postal code to search for (e.g., '8001')

        Returns:
            List of matching PostalLocalityV1 instances

        Examples:
            >>> api = PostalCodesAPI(fallback_allowed=True)
            >>> localities = api.get_by_postal_code('8001')
            >>> for loc in localities:
            ...     print(loc.locality_name)
            Zürich
        """
        postal_code = postal_code.strip()
        return [
            locality for locality in self.iter_all()
            if locality.postal_code == postal_code
        ]

    def get_by_municipality(self, bfs_number: int) -> List[PostalLocalityV1]:
        """Get all localities in a specific municipality.

        Args:
            bfs_number: BFS municipality number (e.g., 261 for Zürich)

        Returns:
            List of matching PostalLocalityV1 instances

        Examples:
            >>> api = PostalCodesAPI(fallback_allowed=True)
            >>> localities = api.get_by_municipality(261)  # Zürich
            >>> len(localities)
            30
            >>> for loc in localities:
            ...     print(f"{loc.postal_code} {loc.locality_name}")
            8001 Zürich
            8002 Zürich
            ...
        """
        return [
            locality for locality in self.iter_all()
            if locality.bfs_number == bfs_number
        ]

    def get_by_canton(self, canton_code: str) -> List[PostalLocalityV1]:
        """Get all localities in a specific canton.

        Args:
            canton_code: Two-letter canton code (e.g., 'ZH', 'GE')

        Returns:
            List of matching PostalLocalityV1 instances

        Examples:
            >>> api = PostalCodesAPI(fallback_allowed=True)
            >>> localities = api.get_by_canton('ZH')
            >>> len(localities)
            388
        """
        canton_code = canton_code.upper().strip()
        return [
            locality for locality in self.iter_all()
            if locality.canton_code == canton_code
        ]

    def iter_by_municipality(self, bfs_number: int) -> Iterator[PostalLocalityV1]:
        """Iterate localities in a specific municipality (memory efficient).

        Args:
            bfs_number: BFS municipality number

        Yields:
            PostalLocalityV1 instances

        Examples:
            >>> api = PostalCodesAPI(fallback_allowed=True)
            >>> for locality in api.iter_by_municipality(261):
            ...     db.insert(locality)
        """
        for locality in self.iter_all():
            if locality.bfs_number == bfs_number:
                yield locality

    def iter_by_canton(self, canton_code: str) -> Iterator[PostalLocalityV1]:
        """Iterate localities in a specific canton (memory efficient).

        Args:
            canton_code: Two-letter canton code

        Yields:
            PostalLocalityV1 instances

        Examples:
            >>> api = PostalCodesAPI(fallback_allowed=True)
            >>> for locality in api.iter_by_canton('ZH'):
            ...     process(locality)
        """
        canton_code = canton_code.upper().strip()
        for locality in self.iter_all():
            if locality.canton_code == canton_code:
                yield locality
