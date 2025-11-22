"""Data models for Swiss official street directory.

Based on: ch.swisstopo.amtliches-strassenverzeichnis
Coordinate System: LV95 (EPSG:2056)
"""

from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional


class StreetV1(BaseModel):
    """Swiss official street from federal directory - Version 1.

    This model represents the canonical structure for Swiss streets as provided
    by the official federal street directory (Amtliches Strassenverzeichnis).

    Data Source:
        ch.swisstopo.amtliches-strassenverzeichnis
        https://data.geo.admin.ch/

    Coordinate System:
        LV95 (EPSG:2056) - Swiss coordinate reference system

    Standards:
        - ESID: Eidgenössischer Strassenidentifikator (Federal Street Identifier)
        - eCH-0010: Postal address standard
        - BFS municipality numbering

    Attributes:
        esid: Eidgenössischer Strassenidentifikator (Federal Street ID)
        name: Official street name
        postal_codes: Associated postal codes (comma-separated with locality)
        municipality_bfs: BFS municipality number
        municipality_name: Official municipality name
        canton_code: Two-letter canton abbreviation
        street_type: Type classification (Street, Square, Path, etc.)
        status: Status (real, planned, historic)
        is_official: Whether this is the official street name
        modified_date: Last modification date
        easting: Easting coordinate in LV95
        northing: Northing coordinate in LV95
        parent_esid: Parent street ESID (for hierarchical streets)
        children_esids: Comma-separated child street ESIDs

    Examples:
        >>> street = StreetV1(
        ...     esid="10194929",
        ...     name="Untere Kirchenholzstrasse",
        ...     postal_codes="8400 Winterthur, 8408 Winterthur",
        ...     municipality_bfs=230,
        ...     municipality_name="Winterthur",
        ...     canton_code="ZH",
        ...     street_type="Street",
        ...     status="real",
        ...     is_official=True,
        ...     modified_date="23.07.2024",
        ...     easting=2695609.382,
        ...     northing=1264330.435,
        ...     parent_esid=None,
        ...     children_esids=None
        ... )
        >>> street.postal_code_list
        ['8400', '8408']

    Version History:
        v1: Initial stable version
    """

    model_config = ConfigDict(
        frozen=True,              # Immutable
        strict=True,              # No type coercion
        str_strip_whitespace=True # Auto-strip whitespace
    )

    # Identification
    esid: str = Field(
        ...,
        description="Eidgenössischer Strassenidentifikator (Federal Street ID)",
        min_length=1,
        max_length=20
    )

    name: str = Field(
        ...,
        description="Official street name (STN_LABEL)",
        min_length=1,
        max_length=200
    )

    # Location
    postal_codes: str = Field(
        ...,
        description="Associated postal codes with localities (ZIP_LABEL)",
        min_length=1,
        max_length=500
    )

    municipality_bfs: int = Field(
        ...,
        description="BFS municipality number (COM_FOSNR)",
        ge=1,
        le=9999
    )

    municipality_name: str = Field(
        ...,
        description="Official municipality name (COM_NAME)",
        min_length=1,
        max_length=100
    )

    canton_code: str = Field(
        ...,
        description="Two-letter canton abbreviation (COM_CANTON)",
        pattern=r'^[A-Z]{2}$'
    )

    # Classification
    street_type: str = Field(
        ...,
        description="Street type (STR_TYPE): Street, Square, Path, etc.",
        min_length=1,
        max_length=50
    )

    status: str = Field(
        ...,
        description="Status (STR_STATUS): real, planned, historic",
        min_length=1,
        max_length=50
    )

    is_official: bool = Field(
        ...,
        description="Whether this is the official street name (STR_OFFICIAL)"
    )

    # Geographic coordinates (LV95)
    easting: float = Field(
        ...,
        description="Easting (E) coordinate in LV95 system (STR_EASTING)",
        ge=2485000.0,
        le=2834000.0
    )

    northing: float = Field(
        ...,
        description="Northing (N) coordinate in LV95 system (STR_NORTHING)",
        ge=1075000.0,
        le=1296000.0
    )

    # Metadata
    modified_date: str = Field(
        ...,
        description="Last modification date (STR_MODIFIED)",
        min_length=1,
        max_length=50
    )

    # Hierarchical relationships
    parent_esid: Optional[str] = Field(
        None,
        description="Parent street ESID (STR_PARENT)",
        max_length=20
    )

    children_esids: Optional[str] = Field(
        None,
        description="Comma-separated child street ESIDs (STR_CHILDREN)",
        max_length=500
    )

    @field_validator('canton_code', mode='before')
    @classmethod
    def uppercase_canton_code(cls, v: str) -> str:
        """Ensure canton code is uppercase."""
        if v:
            return v.upper().strip()
        return v

    @field_validator('is_official', mode='before')
    @classmethod
    def parse_boolean(cls, v) -> bool:
        """Parse boolean from various formats."""
        if isinstance(v, bool):
            return v
        if v is None or v == '':
            return False
        return str(v).lower() in ('true', 'yes', '1', 'j', 'ja')

    @field_validator('parent_esid', 'children_esids', mode='before')
    @classmethod
    def handle_empty_string(cls, v) -> Optional[str]:
        """Convert empty strings to None."""
        if v == '' or v is None:
            return None
        return str(v).strip()

    @property
    def coordinates_lv95(self) -> tuple[float, float]:
        """Get coordinates as (easting, northing) tuple in LV95 system.

        Returns:
            Tuple of (easting, northing) coordinates

        Examples:
            >>> street = StreetV1(easting=2695609.382, northing=1264330.435, ...)
            >>> street.coordinates_lv95
            (2695609.382, 1264330.435)
        """
        return (self.easting, self.northing)

    @property
    def postal_code_list(self) -> list[str]:
        """Extract list of postal codes from postal_codes field.

        The postal_codes field contains entries like "8400 Winterthur, 8408 Winterthur".
        This property extracts just the postal codes.

        Returns:
            List of 4-digit postal codes

        Examples:
            >>> street = StreetV1(postal_codes="8400 Winterthur, 8408 Winterthur", ...)
            >>> street.postal_code_list
            ['8400', '8408']
            >>> street = StreetV1(postal_codes="8001 Zürich", ...)
            >>> street.postal_code_list
            ['8001']
        """
        if not self.postal_codes:
            return []

        codes = []
        for entry in self.postal_codes.split(','):
            entry = entry.strip()
            if entry:
                # Extract first token (postal code)
                parts = entry.split()
                if parts:
                    codes.append(parts[0])

        return codes

    @property
    def has_parent(self) -> bool:
        """Check if this street has a parent street."""
        return self.parent_esid is not None

    @property
    def has_children(self) -> bool:
        """Check if this street has child streets."""
        return self.children_esids is not None

    @property
    def children_esid_list(self) -> list[str]:
        """Get list of child ESIDs.

        Returns:
            List of child street ESIDs

        Examples:
            >>> street = StreetV1(children_esids="10001,10002,10003", ...)
            >>> street.children_esid_list
            ['10001', '10002', '10003']
        """
        if not self.children_esids:
            return []
        return [esid.strip() for esid in self.children_esids.split(',') if esid.strip()]

    def __str__(self) -> str:
        """String representation."""
        return f"{self.name} ({self.municipality_name}, {self.canton_code})"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (
            f"StreetV1(esid='{self.esid}', "
            f"name='{self.name}', "
            f"municipality_bfs={self.municipality_bfs})"
        )


# Placeholder for future version if API changes
# class StreetV2(BaseModel):
#     """V2 model when/if API format changes significantly."""
#     pass
