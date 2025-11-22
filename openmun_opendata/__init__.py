"""OpenMun OpenData - Swiss reference data for municipal administration.

This package provides official Swiss reference data including:
- BFS country codes
- Canton codes
- Municipality history (BFS API)
- Postal codes and localities (geo.admin.ch)
- Official street directory (geo.admin.ch)
- Other Swiss government reference data

Examples:
    >>> # Postal codes
    >>> from openmun_opendata import PostalCodesAPI
    >>> api = PostalCodesAPI(fallback_allowed=True)
    >>> for locality in api.iter_all():
    ...     db.insert(locality)

    >>> # Streets
    >>> from openmun_opendata import StreetsAPI
    >>> api = StreetsAPI(fallback_allowed=True)
    >>> for street in api.iter_by_municipality(261):
    ...     db.insert(street)

    >>> # Municipalities
    >>> from openmun_opendata import MunicipalitiesAPI
    >>> api = MunicipalitiesAPI(fallback_allowed=True)
    >>> for municipality in api.iter_all():
    ...     db.insert(municipality)
"""

__version__ = "0.1.0"

# Geo APIs for data.geo.admin.ch and BFS
from openmun_opendata.geo import (
    PostalCodesAPI,
    PostalLocalityV1,
    StreetsAPI,
    StreetV1,
    MunicipalitiesAPI,
    MunicipalityV1,
)

__all__ = [
    # Geo APIs
    'PostalCodesAPI',
    'StreetsAPI',
    'MunicipalitiesAPI',
    # Geo Models
    'PostalLocalityV1',
    'StreetV1',
    'MunicipalityV1',
]
