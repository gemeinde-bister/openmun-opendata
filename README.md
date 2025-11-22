# OpenMun OpenData

Python package providing Swiss government reference data for municipal administration.

## Overview

This package provides access to official Swiss government data:
- BFS country codes with multilingual names
- Swiss postal codes and localities
- Official street directory
- Municipality history and administrative structure

The package fetches data from official government APIs (data.geo.admin.ch, BFS) and provides it through a clean Python interface. All data models are versioned and validated using Pydantic. Data can be cached locally for offline use.

## Installation

```bash
pip install openmun-opendata
```

For development (includes data import tools):

```bash
pip install openmun-opendata[dev]
```

## Usage

### Country Codes

```python
from openmun_opendata.countries import get_country

switzerland = get_country('CH')
print(switzerland.bfs_code)  # '8100'
print(switzerland.name_de)   # 'Schweiz'
```

### Postal Codes

```python
from openmun_opendata import PostalCodesAPI

api = PostalCodesAPI(fallback_allowed=True)

# Get all localities
for locality in api.iter_all():
    print(f"{locality.postal_code} {locality.locality_name}")

# Filter by postal code or municipality
zurich_localities = api.get_by_postal_code('8001')
municipality_localities = api.get_by_municipality(261)
```

### Streets

```python
from openmun_opendata import StreetsAPI

api = StreetsAPI(fallback_allowed=True)

# Iterate streets in a municipality
for street in api.iter_by_municipality(261):
    print(f"{street.esid}: {street.name}")

# Get specific street by ID
street = api.get_by_esid('10194929')
```

### Municipalities

```python
from openmun_opendata import MunicipalitiesAPI

api = MunicipalitiesAPI(fallback_allowed=True)

# Get all administrative units (cantons, districts, municipalities)
for unit in api.iter_all():
    print(f"{unit.name} ({unit.canton_code})")

# Get specific municipality
zurich = api.get_by_bfs_code('261')
print(f"{zurich.name} is in canton {zurich.canton_code}")

# Filter by canton
zh_units = api.get_by_canton('ZH')

# Historical snapshot
api_2020 = MunicipalitiesAPI(reference_date="01-01-2020", fallback_allowed=True)
```

## Data Models

All data is returned as Pydantic models. Models are versioned (currently v1) and immutable after creation. Fields are strictly typed and validated.

```python
locality = api.get_by_postal_code('8001')[0]
print(type(locality))  # PostalLocalityV1
print(locality.bfs_number)  # 261

# Models are immutable
locality.postal_code = '9999'  # Raises validation error
```

Version pinning is supported for stability:

```python
api = PostalCodesAPI(model_version='v1')
```

## Data Sources

Data is provided by Swiss government agencies:
- BFS (Federal Statistical Office): country codes and municipality data
- swisstopo via data.geo.admin.ch: postal codes and streets

All data is available under Open Government Data (OGD) Switzerland terms. See [DATA_SOURCES.md](DATA_SOURCES.md) for attribution requirements.

## Offline Use

You can pre-download data for offline use:

```bash
python scripts/download_geodata.py
```

Available options:
- `--dataset {postal,streets,municipalities,all}` - Select dataset
- `--reference-date DD-MM-YYYY` - Historical snapshot for municipalities
- `--force` - Force redownload

## Project Structure

```
openmun-opendata/
├── openmun_opendata/
│   ├── countries.py           # Country codes API
│   └── geo/
│       ├── models/
│       │   ├── postal_codes.py    # PostalLocalityV1
│       │   ├── streets.py         # StreetV1
│       │   └── municipalities.py  # MunicipalityV1
│       ├── postal_codes.py    # PostalCodesAPI
│       ├── streets.py         # StreetsAPI
│       └── municipalities.py  # MunicipalitiesAPI
│
├── sources/
│   ├── bfs/                   # BFS source data
│   └── swisstopo/             # Cached geodata
│
├── importers/                 # Data import tools
└── scripts/                   # Utility scripts
```

## Development

Setup:

```bash
git clone https://github.com/openmun/openmun-opendata.git
cd openmun-opendata
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

Run tests:

```bash
pytest tests/
```

Update data:

```bash
python scripts/download_geodata.py --force
python importers/bfs_country_importer.py --force
```

## API Reference

### PostalCodesAPI

- `iter_all()`, `get_all()` - All localities
- `get_by_postal_code(code)` - Filter by postal code
- `get_by_municipality(bfs_number)` - Filter by municipality
- `get_by_canton(code)` - Filter by canton
- `iter_by_municipality(bfs_number)`, `iter_by_canton(code)` - Memory-efficient iterators

### StreetsAPI

- `iter_all()`, `get_all()` - All streets
- `get_by_esid(esid)` - Get street by ID
- `get_by_municipality(bfs_number)` - Filter by municipality
- `get_by_canton(code)` - Filter by canton
- `iter_by_municipality(bfs_number)`, `iter_by_canton(code)` - Memory-efficient iterators
- `iter_by_postal_code(code)` - Filter by postal code

### MunicipalitiesAPI

Constructor parameter:
- `reference_date` - Snapshot date (DD-MM-YYYY format, default: today)

Methods:
- `iter_all()`, `get_all()` - All administrative units
- `get_by_bfs_code(code)` - Get by BFS code
- `get_by_historical_code(code)` - Get by historical code
- `get_by_canton(code)` - Filter by canton
- `get_active()`, `get_historical()` - Filter by status
- `iter_by_canton(code)` - Memory-efficient iterator

### Data Models

**PostalLocalityV1**

Fields: `locality_name`, `postal_code`, `municipality_name`, `bfs_number`, `canton_code`, `easting`, `northing`

Properties: `full_postal_code`, `coordinates_lv95`

**StreetV1**

Fields: `esid`, `name`, `municipality_bfs`, `municipality_name`, `canton_code`, `postal_codes`, `street_type`, `easting`, `northing`

Properties: `postal_code_list`, `coordinates_lv95`

**MunicipalityV1**

Fields: `historical_code`, `bfs_code`, `name`, `short_name`, `canton_code`, `canton_name`, `level`, `parent`, `valid_from`, `valid_to`, `rec_type`

Properties: `is_active`, `is_merged`, `has_parent`

Administrative levels: 1=Canton, 2=District, 3=Municipality

Canton information is automatically enriched by traversing the parent hierarchy.

## License

Code is licensed under the MIT License. See LICENSE file for details.

Data files are subject to Open Government Data (OGD) Switzerland terms. Attribution to original data providers is required. See [DATA_SOURCES.md](DATA_SOURCES.md) for details.

Copyright (c) OpenMun Project

## Contributing

Contributions are welcome. Please maintain source data attribution, follow existing code style, and add tests for new features.

## Credits

Data provided by Swiss Federal Statistical Office (BFS) and Federal Office of Topography (swisstopo).
