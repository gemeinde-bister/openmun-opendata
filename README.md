# OpenMun OpenData

Swiss reference data (BFS, municipalities, cantons) for the OpenMun municipal administration system.

## Overview

This repository provides official Swiss government reference data as a Python package. The data is:
- **Auto-generated** from official sources (BFS Excel files, etc.)
- **Version-tracked** with source metadata
- **Clean API** for easy consumption
- **Minimal dependencies** for end users

## Installation

### For End Users (Public API only)

```bash
pip install openmun-opendata
```

This installs only the package with pre-generated data. No Excel dependencies required!

### For Developers (with importers)

```bash
pip install openmun-opendata[dev]
```

This includes development dependencies (openpyxl, pytest, etc.) for regenerating data from sources.

## Usage

### Country Codes

```python
from openmun_opendata.countries import get_country, get_country_by_bfs, search_countries

# Get country by ISO code
switzerland = get_country('CH')
print(switzerland.bfs_code)  # '8100'
print(switzerland.name_de)   # 'Schweiz'
print(switzerland.name_fr)   # 'Suisse'

# Get country by BFS code
country = get_country_by_bfs('8100')
print(country.iso2)  # 'CH'

# Search countries by name
results = search_countries('Deutsch', 'de')
for country in results:
    print(f"{country.iso2}: {country.name_de}")

# Use pre-defined constants
from openmun_opendata.countries import SWITZERLAND, GERMANY, FRANCE
print(SWITZERLAND.bfs_code)  # '8100'
```

## Data Structure

```
openmun-opendata/
├── sources/              # Original data files (Excel, CSV, etc.)
│   └── bfs/
│       ├── be-b-00.04-sg-01.xlsx  # BFS country codes
│       └── metadata.json           # Source documentation
│
├── importers/           # Scripts to convert sources → Python
│   ├── base.py         # Base importer class
│   └── bfs_country_importer.py
│
├── generated/           # Auto-generated Python modules
│   └── bfs/
│       ├── country_codes.py  # Generated from Excel
│       └── VERSION           # Generation metadata
│
└── openmun_opendata/    # Public API package
    └── countries.py     # Clean API for country data
```

## Updating Data

### 1. Update Source Files

Place new Excel/CSV files in `sources/` directory, keeping original filenames:
```bash
cp new-bfs-data.xlsx sources/bfs/be-b-00.04-sg-01.xlsx
```

### 2. Run Importers

Regenerate Python code from sources:
```bash
# Regenerate country codes
python importers/bfs_country_importer.py --force

# Run all importers (future)
python importers/update_all.py
```

### 3. Run Tests

Verify data integrity:
```bash
pytest tests/
```

### 4. Commit Changes

Both source files and generated code should be committed:
```bash
git add sources/ generated/
git commit -m "Update BFS country codes to 2025 version"
```

## Available Data

### Currently Implemented

- **BFS Country Codes** ✅
  - 249 countries with BFS codes
  - ISO2/ISO3 mappings
  - Names in 4 languages (DE/FR/IT/EN)
  - Source: `be-b-00.04-sg-01.xlsx`

### Planned

- **Canton Data** 🔜
  - Canton codes and abbreviations
  - Names in multiple languages
  - BFS canton IDs (1-26)

- **Municipality Data** 🔜
  - Current municipalities
  - Historical municipality data
  - Mergers and changes

- **Postal Codes** 🔜
  - Swiss Post PLZ directory
  - Street names and localities

## Development

### Project Setup

```bash
# Clone repository
git clone https://github.com/yourusername/openmun-opendata.git
cd openmun-opendata

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=openmun_opendata

# Run specific test
pytest tests/test_countries.py
```

### Adding New Data Sources

1. Create importer in `importers/`
2. Add source files to `sources/`
3. Generate Python code to `generated/`
4. Create public API in `openmun_opendata/`
5. Write tests in `tests/`
6. Update this README

## Design Principles

1. **Source Preservation**: Keep original filenames and structure
2. **Reproducibility**: Always regeneratable from sources
3. **Clean API**: Hide complexity from end users
4. **Minimal Dependencies**: End users don't need Excel libraries
5. **Version Tracking**: Document source versions and dates
6. **Type Safety**: Use dataclasses and type hints

## License

This repository has a dual licensing structure:

### Software Code (MIT License)
- **What:** All Python code, scripts, importers, tests, configuration files
- **License:** MIT License (see LICENSE file)
- **Copyright:** © 2025 OpenMun Project
- **Permissions:** Free to use, modify, distribute for any purpose

### Data Files (Source-Specific Terms)
- **What:** Original source files (`sources/`), generated data (`generated/`), data in package
- **Terms:** Subject to the copyright and terms of use of the respective data providers
- **Attribution Required:** You must credit the original data source when using the data
- **Details:** See DATA_SOURCES.md for complete information

**Important:** When using this package, you are bound by BOTH:
1. The MIT License for the code
2. The data providers' terms of use for the data

For detailed attribution requirements and terms of use for each dataset, see [DATA_SOURCES.md](DATA_SOURCES.md).

## Contributing

Contributions are welcome! Please:
1. Keep original source filenames
2. Document sources in metadata.json
3. Write tests for new data
4. Update documentation

## Credits

Data sources:
- Swiss Federal Statistical Office (BFS)
- Swiss Post
- Federal Office of Topography (swisstopo)