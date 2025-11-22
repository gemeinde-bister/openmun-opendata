#!/usr/bin/env python3
"""Download Swiss geodata from official government sources.

This script downloads various datasets from Swiss government sources:
- Postal localities (swisstopo via data.geo.admin.ch)
- Official street directory (swisstopo via data.geo.admin.ch)
- Municipality history (BFS communes snapshot API)

Data is downloaded to the sources/swisstopo directory.

Usage:
    python scripts/download_geodata.py [--force] [--dataset DATASET] [--reference-date DATE]
"""

import sys
import json
import zipfile
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


class GeoDataDownloader:
    """Downloader for Swiss geodata from official sources."""

    def __init__(self, project_root: Optional[Path] = None, reference_date: Optional[str] = None):
        """Initialize downloader with project root.

        Args:
            project_root: Project root directory
            reference_date: Reference date for municipality snapshot (DD-MM-YYYY)
        """
        self.project_root = project_root or Path(__file__).parent.parent
        self.sources_dir = self.project_root / "sources" / "swisstopo"
        self.base_url = "https://data.geo.admin.ch"
        self.stac_api = f"{self.base_url}/api/stac/v0.9"
        self.bfs_api = "https://www.agvchapp.bfs.admin.ch/api/communes"
        self.reference_date = reference_date or datetime.now().strftime("%d-%m-%Y")

    def ensure_dirs(self):
        """Ensure source directories exist."""
        self.sources_dir.mkdir(parents=True, exist_ok=True)

    def download_file(self, url: str, destination: Path) -> bool:
        """Download a file from URL to destination.

        Args:
            url: URL to download from
            destination: Local file path to save to

        Returns:
            True if download was successful
        """
        print(f"  Downloading from: {url}")
        print(f"  Saving to: {destination}")

        try:
            request = Request(url, headers={'User-Agent': 'OpenMun-OpenData/1.0'})
            with urlopen(request, timeout=60) as response:
                if response.status != 200:
                    print(f"  ERROR: HTTP {response.status}")
                    return False

                # Download in chunks
                chunk_size = 8192
                total_size = int(response.headers.get('Content-Length', 0))
                downloaded = 0

                with open(destination, 'wb') as f:
                    while True:
                        chunk = response.read(chunk_size)
                        if not chunk:
                            break
                        f.write(chunk)
                        downloaded += len(chunk)

                        if total_size > 0:
                            percent = (downloaded / total_size) * 100
                            print(f"  Progress: {percent:.1f}%", end='\r')

                if total_size > 0:
                    print()  # New line after progress

            print(f"  Downloaded {downloaded / 1024 / 1024:.2f} MB")
            return True

        except (HTTPError, URLError) as e:
            print(f"  ERROR: Failed to download: {e}")
            return False
        except Exception as e:
            print(f"  ERROR: {e}")
            return False

    def get_stac_collection_items(self, collection_id: str) -> Optional[Dict[str, Any]]:
        """Fetch STAC collection items from API.

        Args:
            collection_id: STAC collection identifier

        Returns:
            JSON response or None if failed
        """
        url = f"{self.stac_api}/collections/{collection_id}/items"
        print(f"  Fetching STAC items from: {url}")

        try:
            request = Request(url, headers={'User-Agent': 'OpenMun-OpenData/1.0'})
            with urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            print(f"  ERROR: Failed to fetch STAC items: {e}")
            return None

    def extract_zip(self, zip_path: Path, extract_to: Optional[Path] = None) -> bool:
        """Extract a zip file.

        Args:
            zip_path: Path to zip file
            extract_to: Directory to extract to (default: same directory as zip)

        Returns:
            True if extraction was successful
        """
        if extract_to is None:
            extract_to = zip_path.parent

        print(f"  Extracting: {zip_path.name}")

        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"  Extracted to: {extract_to}")
            return True
        except Exception as e:
            print(f"  ERROR: Failed to extract: {e}")
            return False

    def download_postal_localities(self, force: bool = False) -> bool:
        """Download postal localities dataset.

        Args:
            force: Force download even if file exists

        Returns:
            True if download was successful
        """
        print("\n=== Downloading Postal Localities ===")

        filename = "ortschaftenverzeichnis_plz_2056.csv.zip"
        url = f"{self.base_url}/ch.swisstopo-vd.ortschaftenverzeichnis_plz/ortschaftenverzeichnis_plz/{filename}"
        destination = self.sources_dir / filename

        if destination.exists() and not force:
            print(f"  File already exists: {destination}")
            print("  Use --force to redownload")
            return True

        success = self.download_file(url, destination)

        if success:
            # Extract the zip
            self.extract_zip(destination)

        return success

    def download_street_registry(self, force: bool = False) -> bool:
        """Download official street directory via STAC API.

        Args:
            force: Force download even if file exists

        Returns:
            True if download was successful
        """
        print("\n=== Downloading Official Street Directory ===")

        collection_id = "ch.swisstopo.amtliches-strassenverzeichnis"

        # Get items from STAC API
        items_data = self.get_stac_collection_items(collection_id)
        if not items_data:
            return False

        # Find the Switzerland item (not Liechtenstein)
        ch_item = None
        for feature in items_data.get('features', []):
            if feature['id'] == 'amtliches-strassenverzeichnis_ch':
                ch_item = feature
                break

        if not ch_item:
            print("  ERROR: Could not find Switzerland street data")
            return False

        # Get CSV asset
        assets = ch_item.get('assets', {})
        csv_asset = assets.get('amtliches-strassenverzeichnis_ch_2056.csv.zip')

        if not csv_asset:
            print("  ERROR: Could not find CSV asset")
            return False

        url = csv_asset['href']
        filename = "amtliches-strassenverzeichnis_ch_2056.csv.zip"
        destination = self.sources_dir / filename

        if destination.exists() and not force:
            print(f"  File already exists: {destination}")
            print("  Use --force to redownload")
            return True

        success = self.download_file(url, destination)

        if success:
            # Extract the zip
            self.extract_zip(destination)

        return success

    def download_municipalities(self, force: bool = False) -> bool:
        """Download municipality history from BFS API.

        Args:
            force: Force download even if file exists

        Returns:
            True if download was successful
        """
        print("\n=== Downloading Municipality History ===")

        from urllib.parse import urlencode

        # Build filename with reference date
        filename = f"bfs_municipalities_{self.reference_date.replace('-', '')}.csv"
        destination = self.sources_dir / filename

        if destination.exists() and not force:
            print(f"  File already exists: {destination}")
            print("  Use --force to redownload")
            return True

        # Build URL with parameters
        params = {
            'date': self.reference_date,
            'format': 'csv'
        }
        url = f"{self.bfs_api}/snapshot?{urlencode(params)}"

        print(f"  Downloading from: {url}")
        print(f"  Reference date: {self.reference_date}")
        print(f"  Saving to: {destination}")

        try:
            request = Request(url, headers={'User-Agent': 'OpenMun-OpenData/1.0'})
            with urlopen(request, timeout=60) as response:
                if response.status != 200:
                    print(f"  ERROR: HTTP {response.status}")
                    return False

                # Read CSV content
                csv_content = response.read().decode('utf-8-sig')

                # Save to file
                with open(destination, 'w', encoding='utf-8') as f:
                    f.write(csv_content)

                # Count records
                record_count = len(csv_content.splitlines()) - 1  # Subtract header
                print(f"  Downloaded {len(csv_content) / 1024:.2f} KB")
                print(f"  Records: {record_count}")

                return True

        except (HTTPError, URLError) as e:
            print(f"  ERROR: Failed to download: {e}")
            return False
        except Exception as e:
            print(f"  ERROR: {e}")
            return False

    def save_metadata(self, datasets: Dict[str, Dict[str, Any]]) -> bool:
        """Save metadata about downloaded datasets.

        Args:
            datasets: Dictionary of dataset metadata

        Returns:
            True if save was successful
        """
        metadata_path = self.sources_dir / "metadata.json"

        # Load existing metadata if it exists
        existing_metadata = {}
        if metadata_path.exists():
            try:
                with open(metadata_path, 'r', encoding='utf-8') as f:
                    existing_metadata = json.load(f)
            except Exception:
                pass

        # Merge with new metadata
        existing_metadata.update(datasets)

        # Save
        try:
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(existing_metadata, f, indent=2, ensure_ascii=False)
            print(f"\nMetadata saved to: {metadata_path}")
            return True
        except Exception as e:
            print(f"ERROR: Failed to save metadata: {e}")
            return False

    def download_all(self, force: bool = False) -> bool:
        """Download all datasets.

        Args:
            force: Force download even if files exist

        Returns:
            True if all downloads were successful
        """
        self.ensure_dirs()

        results = {
            'postal_localities': self.download_postal_localities(force),
            'street_registry': self.download_street_registry(force),
            'municipalities': self.download_municipalities(force),
        }

        # Update metadata
        municipality_filename = f"bfs_municipalities_{self.reference_date.replace('-', '')}.csv"
        metadata = {
            "ortschaftenverzeichnis_plz_2056.csv.zip": {
                "description": "Swiss Postal Codes and Localities (Ortschaftenverzeichnis PLZ)",
                "source": "swisstopo",
                "dataset_id": "ch.swisstopo-vd.ortschaftenverzeichnis_plz",
                "url": "https://data.geo.admin.ch/ch.swisstopo-vd.ortschaftenverzeichnis_plz/",
                "format": "CSV (semicolon-delimited)",
                "coordinate_system": "LV95 (EPSG:2056)",
                "downloaded": datetime.now().strftime("%Y-%m-%d"),
                "license": "Open Government Data (OGD) Switzerland",
                "update_frequency": "Monthly"
            },
            "amtliches-strassenverzeichnis_ch_2056.csv.zip": {
                "description": "Official Street Directory of Switzerland",
                "source": "swisstopo",
                "dataset_id": "ch.swisstopo.amtliches-strassenverzeichnis",
                "url": "https://data.geo.admin.ch/ch.swisstopo.amtliches-strassenverzeichnis/",
                "format": "CSV",
                "coordinate_system": "LV95 (EPSG:2056)",
                "downloaded": datetime.now().strftime("%Y-%m-%d"),
                "license": "Open Government Data (OGD) Switzerland",
                "notes": ["Contains all Swiss streets with ESID codes"]
            },
            municipality_filename: {
                "description": "Swiss Municipality History (BFS Communes Snapshot)",
                "source": "BFS",
                "dataset_id": "communes.snapshot",
                "url": "https://www.agvchapp.bfs.admin.ch/api/communes/snapshot",
                "format": "CSV (comma-delimited)",
                "reference_date": self.reference_date,
                "downloaded": datetime.now().strftime("%Y-%m-%d"),
                "license": "Open Government Data (OGD) Switzerland",
                "notes": ["Includes current and historical municipalities"]
            }
        }

        self.save_metadata(metadata)

        # Print summary
        print("\n" + "=" * 60)
        print("Download Summary:")
        print("=" * 60)
        for dataset, success in results.items():
            status = "✓ SUCCESS" if success else "✗ FAILED"
            print(f"{dataset:30} {status}")
        print("=" * 60)

        return all(results.values())


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Download Swiss geodata from official government sources'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force download even if files exist'
    )
    parser.add_argument(
        '--dataset',
        choices=['postal', 'streets', 'municipalities', 'all'],
        default='all',
        help='Which dataset to download (default: all)'
    )
    parser.add_argument(
        '--reference-date',
        type=str,
        help='Reference date for municipality snapshot in DD-MM-YYYY format (default: today)'
    )

    args = parser.parse_args()

    downloader = GeoDataDownloader(reference_date=args.reference_date)

    if args.dataset == 'all':
        success = downloader.download_all(force=args.force)
    elif args.dataset == 'postal':
        downloader.ensure_dirs()
        success = downloader.download_postal_localities(force=args.force)
    elif args.dataset == 'streets':
        downloader.ensure_dirs()
        success = downloader.download_street_registry(force=args.force)
    elif args.dataset == 'municipalities':
        downloader.ensure_dirs()
        success = downloader.download_municipalities(force=args.force)
    else:
        print(f"Unknown dataset: {args.dataset}")
        return 1

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
