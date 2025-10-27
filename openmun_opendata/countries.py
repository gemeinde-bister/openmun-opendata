"""Public API for BFS country codes.

This module provides a clean, stable API for accessing Swiss BFS country codes
and their multilingual names. The data is auto-generated from official BFS sources.

Example usage:
    from openmun_opendata.countries import Country, get_country

    # Get country by ISO code
    switzerland = get_country('CH')
    print(switzerland.bfs_code)  # '8207'
    print(switzerland.name_de)   # 'Schweiz'
    print(switzerland.name_fr)   # 'Suisse'

    # Get country by BFS code
    country = get_country_by_bfs('8207')
    print(country.iso2)  # 'CH'

    # Get all countries
    for country in get_all_countries():
        print(f"{country.iso2}: {country.name_en}")
"""

from typing import Optional, List, Dict, Any
from dataclasses import dataclass

# Import generated data
try:
    from generated.bfs.country_codes import COUNTRY_CODES
except ImportError:
    # Fallback for development or if generated files not available
    COUNTRY_CODES = {}


@dataclass
class Country:
    """Country with BFS code and multilingual names."""

    iso2: str
    bfs_code: str
    iso3: str
    name_de: str
    name_fr: str
    name_it: str
    name_en: str

    def get_name(self, language: str = 'de') -> str:
        """Get country name in specified language.

        Args:
            language: Language code ('de', 'fr', 'it', 'en')

        Returns:
            Country name in requested language, falls back to German
        """
        names = {
            'de': self.name_de,
            'fr': self.name_fr,
            'it': self.name_it,
            'en': self.name_en,
        }
        return names.get(language, self.name_de)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            'iso2': self.iso2,
            'iso3': self.iso3,
            'bfs_code': self.bfs_code,
            'names': {
                'de': self.name_de,
                'fr': self.name_fr,
                'it': self.name_it,
                'en': self.name_en,
            }
        }


def get_country(iso_code: str) -> Optional[Country]:
    """Get country by ISO 2-letter code.

    Args:
        iso_code: ISO 3166-1 alpha-2 country code (e.g., 'CH', 'DE')

    Returns:
        Country object or None if not found
    """
    data = COUNTRY_CODES.get(iso_code.upper())
    if data:
        return Country(
            iso2=iso_code.upper(),
            bfs_code=data['bfs_code'],
            iso3=data['iso3'],
            name_de=data['names']['de'],
            name_fr=data['names']['fr'],
            name_it=data['names']['it'],
            name_en=data['names']['en'],
        )
    return None


def get_country_by_bfs(bfs_code: str) -> Optional[Country]:
    """Get country by BFS code.

    Args:
        bfs_code: BFS country code (e.g., '8207' for Switzerland)

    Returns:
        Country object or None if not found
    """
    bfs_str = str(bfs_code)
    for iso2, data in COUNTRY_CODES.items():
        if data['bfs_code'] == bfs_str:
            return Country(
                iso2=iso2,
                bfs_code=data['bfs_code'],
                iso3=data['iso3'],
                name_de=data['names']['de'],
                name_fr=data['names']['fr'],
                name_it=data['names']['it'],
                name_en=data['names']['en'],
            )
    return None


def get_all_countries() -> List[Country]:
    """Get all countries.

    Returns:
        List of all Country objects, sorted by ISO2 code
    """
    countries = []
    for iso2 in sorted(COUNTRY_CODES.keys()):
        country = get_country(iso2)
        if country:
            countries.append(country)
    return countries


def search_countries(query: str, language: str = 'de') -> List[Country]:
    """Search countries by name.

    Args:
        query: Search query (case-insensitive partial match)
        language: Language to search in ('de', 'fr', 'it', 'en')

    Returns:
        List of matching countries
    """
    query_lower = query.lower()
    results = []

    for country in get_all_countries():
        name = country.get_name(language)
        if query_lower in name.lower():
            results.append(country)

    return results


# Common country codes for convenience
SWITZERLAND = get_country('CH')
GERMANY = get_country('DE')
FRANCE = get_country('FR')
ITALY = get_country('IT')
AUSTRIA = get_country('AT')
LIECHTENSTEIN = get_country('LI')


# Re-export raw data for advanced usage
__all__ = [
    'Country',
    'get_country',
    'get_country_by_bfs',
    'get_all_countries',
    'search_countries',
    'SWITZERLAND',
    'GERMANY',
    'FRANCE',
    'ITALY',
    'AUSTRIA',
    'LIECHTENSTEIN',
]