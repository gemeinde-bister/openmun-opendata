"""Base importer class for data conversion."""

from pathlib import Path
from datetime import datetime
from typing import Optional, Any, Dict
import json


class BaseImporter:
    """Base class for data importers."""

    def __init__(self, project_root: Optional[Path] = None):
        """Initialize importer with project root."""
        self.project_root = project_root or Path(__file__).parent.parent
        self.sources_dir = self.project_root / "sources"
        self.generated_dir = self.project_root / "generated"

    def read_metadata(self, source_type: str) -> Dict[str, Any]:
        """Read metadata for a source type."""
        metadata_path = self.sources_dir / source_type / "metadata.json"
        if metadata_path.exists():
            with open(metadata_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def write_version_file(self, output_dir: Path, source_file: str, metadata: Optional[Dict] = None):
        """Write VERSION file to track generation."""
        version_file = output_dir / "VERSION"
        with open(version_file, 'w', encoding='utf-8') as f:
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Source: {source_file}\n")
            if metadata:
                f.write(f"Source Version: {metadata.get('version', 'unknown')}\n")
                f.write(f"Downloaded: {metadata.get('downloaded', 'unknown')}\n")

    def ensure_init_files(self, *dirs: Path):
        """Ensure __init__.py exists in directories."""
        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)
            init_file = dir_path / "__init__.py"
            if not init_file.exists():
                init_file.write_text('"""Auto-generated data."""\n')

    def generate_python_header(self, source_file: str, description: str = "",
                               data_provider: str = "Swiss Federal Statistical Office (BFS)",
                               data_url: str = "https://www.bfs.admin.ch/",
                               data_year: str = "2024",
                               importer_script: str = "bfs_country_importer.py") -> str:
        """Generate standard Python file header with data attribution."""
        return f'''"""Auto-generated from BFS data.

DO NOT EDIT MANUALLY!

Generated: {datetime.now().isoformat()}
Source: {source_file}
Description: {description}

DATA SOURCE ATTRIBUTION:
    Data Provider: {data_provider}
    Dataset: {description}
    Terms of Use: Open Government Data (OGD) Switzerland - "Open use. Must provide the source."
    URL: {data_url}
    Copyright: © {data_year} {data_provider}

    This data is made available under Swiss OGD terms, which require source attribution.
    See DATA_SOURCES.md in the repository root for complete licensing information.

CODE LICENSE:
    This Python code structure is © 2025 OpenMun Project, licensed under MIT License.
    The data content is © {data_provider}, used under OGD terms.

Run importers/{importer_script} to regenerate.
"""

'''