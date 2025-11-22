"""Data models for Swiss geodata APIs.

These models represent the canonical data structures for Swiss government geodata.
Models are versioned (V1, V2, etc.) to handle format evolution over time.
"""

from openmun_opendata.geo.models.postal_codes import PostalLocalityV1
from openmun_opendata.geo.models.streets import StreetV1
from openmun_opendata.geo.models.municipalities import MunicipalityV1

__all__ = [
    'PostalLocalityV1',
    'StreetV1',
    'MunicipalityV1',
]
