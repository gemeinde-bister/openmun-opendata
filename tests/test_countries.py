"""Tests for country codes API."""

import pytest
from openmun_opendata.countries import (
    Country,
    get_country,
    get_country_by_bfs,
    get_all_countries,
    search_countries,
    SWITZERLAND,
)


def test_get_country_switzerland():
    """Test getting Switzerland by ISO code."""
    ch = get_country('CH')
    assert ch is not None
    assert ch.iso2 == 'CH'
    assert ch.iso3 == 'CHE'
    assert ch.bfs_code == '8100'  # Official BFS code for Switzerland
    assert ch.name_de == 'Schweiz'
    assert ch.name_fr == 'Suisse'
    assert ch.name_it == 'Svizzera'
    assert ch.name_en == 'Switzerland'


def test_get_country_case_insensitive():
    """Test that ISO codes are case-insensitive."""
    ch1 = get_country('ch')
    ch2 = get_country('CH')
    ch3 = get_country('Ch')

    assert ch1 is not None
    assert ch2 is not None
    assert ch3 is not None
    assert ch1.bfs_code == ch2.bfs_code == ch3.bfs_code


def test_get_country_by_bfs():
    """Test getting country by BFS code."""
    ch = get_country_by_bfs('8100')  # Switzerland's actual BFS code
    assert ch is not None
    assert ch.iso2 == 'CH'
    assert ch.name_de == 'Schweiz'

    # Also test Germany
    de = get_country_by_bfs('8207')  # Germany's BFS code
    assert de is not None
    assert de.iso2 == 'DE'
    assert de.name_de == 'Deutschland'


def test_get_country_invalid():
    """Test getting non-existent country."""
    assert get_country('XX') is None
    assert get_country_by_bfs('9999') is None


def test_get_all_countries():
    """Test getting all countries."""
    countries = get_all_countries()
    assert len(countries) > 200  # Should have 249 countries

    # Check they're sorted
    iso_codes = [c.iso2 for c in countries]
    assert iso_codes == sorted(iso_codes)

    # Check some known countries exist
    iso_set = set(iso_codes)
    assert 'CH' in iso_set
    assert 'DE' in iso_set
    assert 'FR' in iso_set
    assert 'US' in iso_set


def test_search_countries():
    """Test searching countries by name."""
    # Search for "Schweiz" in German
    results = search_countries('Schweiz', 'de')
    assert len(results) == 1
    assert results[0].iso2 == 'CH'

    # Search for "Suisse" in French
    results = search_countries('Suisse', 'fr')
    assert len(results) == 1
    assert results[0].iso2 == 'CH'

    # Partial match
    results = search_countries('Schw', 'de')
    assert len(results) >= 1
    assert any(c.iso2 == 'CH' for c in results)

    # Case-insensitive
    results = search_countries('SCHWEIZ', 'de')
    assert len(results) == 1
    assert results[0].iso2 == 'CH'


def test_country_get_name():
    """Test getting country name in different languages."""
    ch = get_country('CH')
    assert ch.get_name('de') == 'Schweiz'
    assert ch.get_name('fr') == 'Suisse'
    assert ch.get_name('it') == 'Svizzera'
    assert ch.get_name('en') == 'Switzerland'

    # Unknown language falls back to German
    assert ch.get_name('xx') == 'Schweiz'


def test_country_to_dict():
    """Test converting country to dictionary."""
    ch = get_country('CH')
    data = ch.to_dict()

    assert data['iso2'] == 'CH'
    assert data['iso3'] == 'CHE'
    assert data['bfs_code'] == '8100'
    assert data['names']['de'] == 'Schweiz'
    assert data['names']['fr'] == 'Suisse'


def test_constant_countries():
    """Test pre-defined country constants."""
    assert SWITZERLAND is not None
    assert SWITZERLAND.iso2 == 'CH'
    assert SWITZERLAND.bfs_code == '8100'


def test_data_integrity():
    """Test that all countries have required data."""
    for country in get_all_countries():
        # All fields should be non-empty
        assert country.iso2
        assert country.bfs_code
        # iso3 might be empty for some territories
        # assert country.iso3

        # At least one name should be present
        assert country.name_de or country.name_fr or country.name_it or country.name_en

        # BFS code should be numeric string
        assert country.bfs_code.isdigit()
        assert len(country.bfs_code) == 4