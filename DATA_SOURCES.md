# Data Sources and Licensing

This document describes the data sources used in this package and their respective licensing terms.

## Important Notice

**The MIT License applies ONLY to the software code** (Python scripts, importers, API wrappers, tests, configuration files).

**The data files and datasets** are subject to the copyright and terms of use of their respective data providers as described below.

## Copyright and Data Protection

In Switzerland, raw data and datasets are generally not protected by copyright (Art. 2 URG). However, data providers may impose terms of use that users must comply with.

## Data Sources

### 1. BFS Country and Territory Codes

**Source Files:**
- `sources/bfs/be-b-00.04-sg-01.xlsx`
- `generated/bfs/country_codes.py`

**Data Provider:**
Swiss Federal Statistical Office (Bundesamt für Statistik - BFS)

**Dataset:**
BFS Official Country and Territory Codes (Staaten- und Gebietsverzeichnis)

**Terms of Use:**
Open Government Data (OGD) Switzerland

**Attribution:**
```
Swiss Federal Statistical Office (BFS) - Country and Territory Codes
Source: https://www.bfs.admin.ch/
```

**Permissions:**
- Non-commercial use
- Commercial use
- Redistribution
- Modification
- **Required:** Source attribution

### 2. Swiss Postal Codes and Localities

**Source:** Cached in `sources/swisstopo/`

**Data Provider:**
Federal Office of Topography (swisstopo)

**Dataset:**
`ch.swisstopo-vd.ortschaftenverzeichnis_plz`

**Access:**
https://data.geo.admin.ch/

**Terms of Use:**
Open Government Data (OGD) Switzerland

**Attribution:**
```
Federal Office of Topography (swisstopo) - Postal Localities Directory
Source: https://data.geo.admin.ch/
```

**Content:**
- 5,700+ localities with postal codes
- LV95 coordinates
- Municipality affiliations
- Canton codes
- Update frequency: Monthly

**Permissions:**
- Non-commercial use
- Commercial use
- Redistribution
- Modification
- **Required:** Source attribution

### 3. Official Street Directory

**Source:** Cached in `sources/swisstopo/`

**Data Provider:**
Federal Office of Topography (swisstopo)

**Dataset:**
`ch.swisstopo.amtliches-strassenverzeichnis`

**Access:**
https://data.geo.admin.ch/

**Terms of Use:**
Open Government Data (OGD) Switzerland

**Attribution:**
```
Federal Office of Topography (swisstopo) - Official Street Directory
Source: https://data.geo.admin.ch/
```

**Content:**
- 220,000+ official street names
- Federal Street Identifiers (ESID)
- LV95 coordinates
- Municipality affiliations
- Associated postal codes

**Permissions:**
- Non-commercial use
- Commercial use
- Redistribution
- Modification
- **Required:** Source attribution

### 4. Municipality History

**Source:** Cached in `sources/swisstopo/`

**Data Provider:**
Swiss Federal Statistical Office (Bundesamt für Statistik - BFS)

**Dataset:**
BFS Communes Snapshot API

**Access:**
https://www.agvchapp.bfs.admin.ch/api/communes/snapshot

**Terms of Use:**
Open Government Data (OGD) Switzerland

**Attribution:**
```
Swiss Federal Statistical Office (BFS) - Communes Snapshot
Source: https://www.agvchapp.bfs.admin.ch/
```

**Content:**
- Current and historical municipalities
- Administrative hierarchy (cantons, districts, municipalities)
- BFS numbers and historical codes
- Validity periods for tracking changes and mergers
- Update frequency: Real-time snapshots

**Permissions:**
- Non-commercial use
- Commercial use
- Redistribution
- Modification
- **Required:** Source attribution

## General Requirements

When using data from this package:

1. **Provide attribution** to the original data source as specified above
2. **Retain copyright notices** in derived works
3. **Do not claim** endorsement by data providers
4. **Check for updates** periodically

## Attribution Format

For publications, websites, or applications:

```
Data source: [Provider Name] - [Dataset Title]
Via: openmun-opendata package
```

Example:
```
Data source: swisstopo - Postal Localities Directory
Via: openmun-opendata package
```

## Data Updates

The package provides tools to download current data from official sources:

```bash
# Download latest geodata
python scripts/download_geodata.py

# Update BFS country codes
python importers/bfs_country_importer.py --force
```

## Questions

For questions about:
- **Software licensing:** See LICENSE file
- **Data terms of use:** Contact the respective data provider
- **Swiss OGD policy:** Visit https://opendata.swiss/

## Legal Disclaimer

This package is provided "as is" without warranty. The OpenMun Project is not responsible for the accuracy, completeness, or fitness for purpose of the source data. Users are responsible for ensuring compliance with all applicable terms and laws.
