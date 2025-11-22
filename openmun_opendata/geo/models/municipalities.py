"""Data models for Swiss municipality history.

Based on: BFS Communes Snapshot API
Source: Federal Statistical Office (BFS)
"""

from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from datetime import date


class MunicipalityV1(BaseModel):
    """Swiss municipality from BFS snapshot - Version 1.

    This model represents the canonical structure for Swiss municipalities
    as provided by the Federal Statistical Office (BFS) via their communes
    snapshot API. Includes both current and historical municipalities.

    Data Source:
        BFS Communes Snapshot API
        https://www.agvchapp.bfs.admin.ch/api/communes/snapshot

    Standards:
        - BFS municipality numbering
        - Historical codes for tracking mergers and changes

    Attributes:
        historical_code: Historical municipality code (unique identifier)
        bfs_code: Current BFS municipality number (null for historical/merged)
        name: Official municipality name
        short_name: Abbreviated municipality name
        canton_code: Two-letter canton code (enriched via parent hierarchy)
        canton_name: Canton name (enriched via parent hierarchy)
        valid_from: Date from which this record is valid
        valid_to: Date until which this record is valid (null if active)
        level: Administrative level (1=Canton, 2=District, 3=Municipality)
        parent: Parent administrative unit code
        rec_type: Record type classification

    Examples:
        >>> municipality = MunicipalityV1(
        ...     historical_code="261",
        ...     bfs_code="261",
        ...     name="Zürich",
        ...     short_name="Zürich",
        ...     canton_code="ZH",
        ...     canton_name="Zürich",
        ...     valid_from=date(1848, 9, 12),
        ...     valid_to=None,
        ...     level=3,
        ...     parent="101",
        ...     rec_type="Commune"
        ... )
        >>> municipality.is_active
        True
        >>> municipality.canton_code
        'ZH'

    Version History:
        v1: Initial stable version
    """

    model_config = ConfigDict(
        frozen=True,              # Immutable
        strict=True,              # No type coercion
        str_strip_whitespace=True # Auto-strip whitespace
    )

    # Identification
    historical_code: str = Field(
        ...,
        description="Historical municipality code (HistoricalCode)",
        min_length=1,
        max_length=12
    )

    bfs_code: Optional[str] = Field(
        None,
        description="Current BFS municipality number (BfsCode), null for merged/historical",
        max_length=12
    )

    # Names
    name: str = Field(
        ...,
        description="Official municipality name (Name)",
        min_length=1,
        max_length=120
    )

    short_name: Optional[str] = Field(
        None,
        description="Abbreviated municipality name (ShortName)",
        max_length=120
    )

    # Canton information (enriched via parent hierarchy)
    canton_code: Optional[str] = Field(
        None,
        description="Two-letter canton code (enriched from parent hierarchy)",
        pattern=r'^([A-Z]{2}|)$'
    )

    canton_name: Optional[str] = Field(
        None,
        description="Canton name (enriched from parent hierarchy)",
        max_length=120
    )

    # Administrative hierarchy
    level: Optional[int] = Field(
        None,
        description="Administrative level (Level): 1=Canton, 2=District, 3=Municipality",
        ge=1,
        le=9
    )

    parent: Optional[str] = Field(
        None,
        description="Parent administrative unit code (Parent)",
        max_length=12
    )

    # Validity period
    valid_from: Optional[date] = Field(
        None,
        description="Date from which this record is valid (ValidFrom)"
    )

    valid_to: Optional[date] = Field(
        None,
        description="Date until which this record is valid (ValidTo), null if currently active"
    )

    # Metadata
    rec_type: Optional[str] = Field(
        None,
        description="Record type classification (Rec_Type_de)",
        max_length=50
    )

    @field_validator('bfs_code', 'short_name', 'canton_code', 'canton_name', 'parent', 'rec_type', mode='before')
    @classmethod
    def handle_empty_string(cls, v) -> Optional[str]:
        """Convert empty strings to None."""
        if v == '' or v is None:
            return None
        return str(v).strip() if str(v).strip() else None

    @field_validator('valid_from', 'valid_to', mode='before')
    @classmethod
    def parse_date(cls, v) -> Optional[date]:
        """Parse date from various formats.

        Supports:
        - DD-MM-YYYY (BFS API format)
        - YYYY-MM-DD (ISO format)
        - DD.MM.YYYY (Swiss format)
        - date objects
        """
        if v is None or v == '':
            return None

        if isinstance(v, date):
            return v

        if isinstance(v, str):
            v = v.strip()
            if not v:
                return None

            # Try DD-MM-YYYY (BFS format)
            if '-' in v and len(v.split('-')) == 3:
                parts = v.split('-')
                if len(parts[0]) <= 2:  # DD-MM-YYYY
                    try:
                        return date(int(parts[2]), int(parts[1]), int(parts[0]))
                    except (ValueError, IndexError):
                        pass
                else:  # YYYY-MM-DD
                    try:
                        return date(int(parts[0]), int(parts[1]), int(parts[2]))
                    except (ValueError, IndexError):
                        pass

            # Try DD.MM.YYYY (Swiss format)
            if '.' in v:
                parts = v.split('.')
                try:
                    return date(int(parts[2]), int(parts[1]), int(parts[0]))
                except (ValueError, IndexError):
                    pass

        # If we get here, we couldn't parse it
        return None

    @property
    def is_active(self) -> bool:
        """Check if this municipality is currently active.

        Returns:
            True if valid_to is None (no end date)

        Examples:
            >>> municipality = MunicipalityV1(valid_to=None, ...)
            >>> municipality.is_active
            True
            >>> municipality = MunicipalityV1(valid_to=date(2020, 1, 1), ...)
            >>> municipality.is_active
            False
        """
        return self.valid_to is None

    @property
    def is_merged(self) -> bool:
        """Check if this municipality has been merged (no longer exists).

        Returns:
            True if valid_to is set and bfs_code is None

        Examples:
            >>> municipality = MunicipalityV1(valid_to=date(2020, 1, 1), bfs_code=None, ...)
            >>> municipality.is_merged
            True
        """
        return self.valid_to is not None and self.bfs_code is None

    @property
    def has_parent(self) -> bool:
        """Check if this municipality has a parent administrative unit."""
        return self.parent is not None

    def __str__(self) -> str:
        """String representation."""
        status = "active" if self.is_active else "historical"
        level_name = {1: "Canton", 2: "District", 3: "Municipality"}.get(self.level, f"Level {self.level}")
        canton_info = f", {self.canton_code}" if self.canton_code else ""
        return f"{self.name} ({level_name}{canton_info}) - {status}"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (
            f"MunicipalityV1(historical_code='{self.historical_code}', "
            f"bfs_code='{self.bfs_code}', "
            f"name='{self.name}')"
        )


# Placeholder for future version if API changes
# class MunicipalityV2(BaseModel):
#     """V2 model when/if API format changes significantly."""
#     pass
