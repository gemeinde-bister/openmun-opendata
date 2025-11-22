"""Swiss geodata APIs for data.geo.admin.ch and BFS datasets.

This module provides clean APIs for accessing Swiss government geodata:
- Postal codes and localities (swisstopo)
- Official street directory (swisstopo)
- Municipality history (BFS)

All APIs support:
- Remote fetching from official sources
- Automatic caching
- Fallback to local cached data
- Versioned data models (V1, V2, etc.)
- Streaming for memory efficiency
"""

# Data models
from openmun_opendata.geo.models.postal_codes import PostalLocalityV1
from openmun_opendata.geo.models.streets import StreetV1
from openmun_opendata.geo.models.municipalities import MunicipalityV1

# APIs
from openmun_opendata.geo.postal_codes import PostalCodesAPI
from openmun_opendata.geo.streets import StreetsAPI
from openmun_opendata.geo.municipalities import MunicipalitiesAPI

__all__ = [
    # Models
    'PostalLocalityV1',
    'StreetV1',
    'MunicipalityV1',
    # APIs
    'PostalCodesAPI',
    'StreetsAPI',
    'MunicipalitiesAPI',
]
