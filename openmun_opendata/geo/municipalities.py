"""API for Swiss municipality history (BFS Communes Snapshot)."""

from typing import Iterator, List, Literal, Optional, Dict
from datetime import datetime
from openmun_opendata.geo.base import BaseGeoAPI
from openmun_opendata.geo.models.municipalities import MunicipalityV1


class MunicipalitiesAPI(BaseGeoAPI):
    """API for accessing Swiss municipality history from BFS.

    This API provides access to the official Swiss municipality directory
    including historical data from the Federal Statistical Office (BFS).
    Data is fetched from the BFS communes snapshot API and can fall back
    to cached data if unavailable.

    Data Source:
        BFS Communes Snapshot API
        https://www.agvchapp.bfs.admin.ch/api/communes/snapshot
        Update Frequency: Real-time (on-demand snapshots)

    Model Versions:
        v1: Current stable version (default)

    Examples:
        >>> # Get current municipalities
        >>> api = MunicipalitiesAPI()
        >>> for municipality in api.iter_all():
        ...     db.insert(municipality)

        >>> # Get historical snapshot
        >>> api = MunicipalitiesAPI(reference_date="01-01-2020")
        >>> municipalities = api.get_all()

        >>> # With fallback to cached data
        >>> api = MunicipalitiesAPI(fallback_allowed=True)
        >>> zurich = api.get_by_bfs_code("261")

        >>> # Filter by canton
        >>> api = MunicipalitiesAPI(fallback_allowed=True)
        >>> zh_municipalities = api.get_by_canton("ZH")

    Attributes:
        model_version: Model version to use ('v1' currently)
        reference_date: Snapshot date in DD-MM-YYYY format (None = latest)
        fallback_allowed: Whether to use cached data if remote fetch fails
    """

    def __init__(
        self,
        reference_date: Optional[str] = None,
        model_version: Literal['v1'] = 'v1',
        fallback_allowed: bool = False,
        **kwargs
    ):
        """Initialize Municipalities API.

        Args:
            reference_date: Snapshot date in DD-MM-YYYY format (e.g., "01-01-2025").
                           None uses the latest available data.
            model_version: Model version to use (only 'v1' currently available)
            fallback_allowed: Allow using cached data if remote fetch fails
            **kwargs: Additional arguments passed to BaseGeoAPI
        """
        super().__init__(fallback_allowed=fallback_allowed, **kwargs)
        self.model_version = model_version
        self.reference_date = reference_date or self._get_current_date()

        # Setup version-specific configuration
        self._setup_version()

        # Cache for enriched municipalities
        self._enriched_cache: Optional[List[MunicipalityV1]] = None

    def _get_current_date(self) -> str:
        """Get current date in DD-MM-YYYY format."""
        return datetime.now().strftime("%d-%m-%Y")

    def _setup_version(self):
        """Setup version-specific dataset parameters."""
        if self.model_version == 'v1':
            # V1 configuration
            self.api_base_url = "https://www.agvchapp.bfs.admin.ch/api/communes"
            self.csv_filename = f"bfs_municipalities_{self.reference_date.replace('-', '')}.csv"
            self.csv_delimiter = ','
            self._parse_row_func = self._parse_row_v1
        else:
            from openmun_opendata.geo.base import GeoAPIError
            raise GeoAPIError(f"Unsupported model version: {self.model_version}")

    def _fetch_remote(self) -> str:
        """Fetch municipality CSV from BFS API.

        Returns:
            CSV content as string

        Raises:
            RemoteFetchError: If fetch fails
        """
        from urllib.request import urlopen, Request
        from urllib.parse import urlencode

        # Build URL with parameters
        params = {
            'date': self.reference_date,
            'format': 'csv'
        }
        url = f"{self.api_base_url}/snapshot?{urlencode(params)}"

        try:
            # Download CSV (not zipped, direct CSV response)
            request = Request(url, headers={'User-Agent': 'OpenMun-OpenData/1.0'})
            with urlopen(request, timeout=30) as response:
                if response.status != 200:
                    from openmun_opendata.geo.base import RemoteFetchError
                    raise RemoteFetchError(f"HTTP {response.status}: {url}")

                csv_content = response.read().decode('utf-8-sig')

                # Cache the downloaded CSV
                cache_path = self.cache_dir / self.csv_filename
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                with open(cache_path, 'w', encoding='utf-8') as f:
                    f.write(csv_content)

                return csv_content

        except Exception as e:
            from openmun_opendata.geo.base import RemoteFetchError
            raise RemoteFetchError(f"Failed to fetch from BFS API: {e}")

    def _fetch_fallback(self) -> str:
        """Get municipality CSV from local cache.

        Returns:
            CSV content as string

        Raises:
            NoFallbackDataError: If local file not found
        """
        return self._read_local_csv(self.csv_filename, from_zip=False)

    def _parse_row_v1(self, row: dict) -> MunicipalityV1:
        """Parse CSV row into MunicipalityV1 model.

        Args:
            row: CSV row as dictionary

        Returns:
            MunicipalityV1 instance (without canton enrichment)

        Note:
            The BFS API provides administrative hierarchy through Level and Parent fields:
            - Level 1 = Canton (ShortName contains canton code)
            - Level 2 = District
            - Level 3 = Municipality

            Canton information is enriched separately via _enrich_with_cantons()
        """
        # BFS API actual header names
        return MunicipalityV1(
            historical_code=row.get('HistoricalCode', ''),
            bfs_code=row.get('BfsCode') or None,
            name=row.get('Name', ''),
            short_name=row.get('ShortName') or None,
            canton_code=None,  # Will be enriched
            canton_name=None,  # Will be enriched
            valid_from=row.get('ValidFrom') or None,
            valid_to=row.get('ValidTo') or None,
            level=int(row['Level']) if row.get('Level') and row['Level'].strip() else None,
            parent=row.get('Parent') or None,
            rec_type=row.get('Rec_Type_de') or None
        )

    def _enrich_with_cantons(self, municipalities: List[MunicipalityV1]) -> List[MunicipalityV1]:
        """Enrich municipalities with canton information by traversing parent hierarchy.

        Args:
            municipalities: List of unenriched municipality records

        Returns:
            List of municipality records with canton_code and canton_name filled in
        """
        # Build lookups for quick access
        by_historical_code: Dict[str, MunicipalityV1] = {
            m.historical_code: m for m in municipalities
        }

        # Build canton lookup (Level 1 entries)
        canton_by_historical_code: Dict[str, tuple[str, str]] = {}
        for m in municipalities:
            if m.level == 1:
                # Canton level: ShortName is the canton code, Name is canton name
                canton_code = m.short_name if m.short_name else None
                canton_name = m.name
                canton_by_historical_code[m.historical_code] = (canton_code, canton_name)

        # Enrich all records with canton info
        enriched = []
        for m in municipalities:
            # Find canton by traversing up the hierarchy
            canton_code = None
            canton_name = None

            if m.level == 1:
                # This IS a canton
                canton_code = m.short_name
                canton_name = m.name
            elif m.parent:
                # Traverse up to find canton
                current = m
                max_depth = 5  # Safety limit
                depth = 0

                while current.parent and depth < max_depth:
                    parent_historical_code = current.parent
                    parent = by_historical_code.get(parent_historical_code)

                    if not parent:
                        break

                    if parent.level == 1:
                        # Found the canton
                        canton_code = parent.short_name
                        canton_name = parent.name
                        break

                    current = parent
                    depth += 1

            # Create enriched copy using model_copy with update
            enriched_m = m.model_copy(update={
                'canton_code': canton_code,
                'canton_name': canton_name
            })
            enriched.append(enriched_m)

        return enriched

    def _get_enriched_data(self) -> List[MunicipalityV1]:
        """Get all municipalities enriched with canton information.

        Returns:
            Cached list of enriched municipalities
        """
        if self._enriched_cache is not None:
            return self._enriched_cache

        # Fetch CSV
        csv_content = self._fetch_or_fallback(
            self._fetch_remote,
            self._fetch_fallback,
            error_context="municipality data"
        )

        # Parse all rows (unenriched)
        unenriched = []
        for row in self._parse_csv(csv_content, delimiter=self.csv_delimiter):
            unenriched.append(self._parse_row_func(row))

        # Enrich with canton information
        enriched = self._enrich_with_cantons(unenriched)

        # Cache for future use
        self._enriched_cache = enriched

        return enriched

    def iter_all(self) -> Iterator[MunicipalityV1]:
        """Iterate over all municipalities in the snapshot.

        All records are enriched with canton information.

        Yields:
            MunicipalityV1 instances with canton_code and canton_name populated

        Examples:
            >>> api = MunicipalitiesAPI(fallback_allowed=True)
            >>> for municipality in api.iter_all():
            ...     print(f"{municipality.name} ({municipality.canton_code}): {municipality.bfs_code}")
        """
        yield from self._get_enriched_data()

    def get_all(self) -> List[MunicipalityV1]:
        """Get all municipalities as a list.

        All records are enriched with canton information.

        Returns:
            List of MunicipalityV1 instances with canton_code and canton_name populated

        Examples:
            >>> api = MunicipalitiesAPI(fallback_allowed=True)
            >>> municipalities = api.get_all()
            >>> print(f"Total: {len(municipalities)}")
            >>> zurich = [m for m in municipalities if m.bfs_code == '261'][0]
            >>> print(f"Canton: {zurich.canton_code}")
        """
        return self._get_enriched_data()

    def get_by_bfs_code(self, bfs_code: str) -> Optional[MunicipalityV1]:
        """Get municipality by BFS code.

        Args:
            bfs_code: BFS municipality number

        Returns:
            MunicipalityV1 instance or None if not found

        Examples:
            >>> api = MunicipalitiesAPI(fallback_allowed=True)
            >>> zurich = api.get_by_bfs_code("261")
            >>> print(zurich.name)  # "Zürich"
        """
        for municipality in self.iter_all():
            if municipality.bfs_code == bfs_code:
                return municipality
        return None

    def get_by_historical_code(self, historical_code: str) -> Optional[MunicipalityV1]:
        """Get municipality by historical code.

        Args:
            historical_code: Historical municipality code

        Returns:
            MunicipalityV1 instance or None if not found

        Examples:
            >>> api = MunicipalitiesAPI(fallback_allowed=True)
            >>> municipality = api.get_by_historical_code("261")
        """
        for municipality in self.iter_all():
            if municipality.historical_code == historical_code:
                return municipality
        return None

    def get_by_canton(self, canton_code: str) -> List[MunicipalityV1]:
        """Get all municipalities in a canton.

        Args:
            canton_code: Two-letter canton code (e.g., "ZH")

        Returns:
            List of MunicipalityV1 instances

        Examples:
            >>> api = MunicipalitiesAPI(fallback_allowed=True)
            >>> zh_municipalities = api.get_by_canton("ZH")
            >>> print(f"Zurich has {len(zh_municipalities)} municipalities")
        """
        canton_upper = canton_code.upper()
        return [
            municipality for municipality in self.iter_all()
            if municipality.canton_code == canton_upper
        ]

    def get_active(self) -> List[MunicipalityV1]:
        """Get all currently active municipalities.

        Returns:
            List of active MunicipalityV1 instances

        Examples:
            >>> api = MunicipalitiesAPI(fallback_allowed=True)
            >>> active = api.get_active()
            >>> print(f"Active municipalities: {len(active)}")
        """
        return [
            municipality for municipality in self.iter_all()
            if municipality.is_active
        ]

    def get_historical(self) -> List[MunicipalityV1]:
        """Get all historical (inactive) municipalities.

        Returns:
            List of historical MunicipalityV1 instances

        Examples:
            >>> api = MunicipalitiesAPI(fallback_allowed=True)
            >>> historical = api.get_historical()
            >>> print(f"Historical municipalities: {len(historical)}")
        """
        return [
            municipality for municipality in self.iter_all()
            if not municipality.is_active
        ]

    def iter_by_canton(self, canton_code: str) -> Iterator[MunicipalityV1]:
        """Iterate municipalities in a canton (memory efficient).

        Args:
            canton_code: Two-letter canton code

        Yields:
            MunicipalityV1 instances for the specified canton

        Examples:
            >>> api = MunicipalitiesAPI(fallback_allowed=True)
            >>> for municipality in api.iter_by_canton("ZH"):
            ...     print(municipality.name)
        """
        canton_upper = canton_code.upper()
        for municipality in self.iter_all():
            if municipality.canton_code == canton_upper:
                yield municipality
