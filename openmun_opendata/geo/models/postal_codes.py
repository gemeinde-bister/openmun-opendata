"""Data models for Swiss postal codes and localities.

Based on: ch.swisstopo-vd.ortschaftenverzeichnis_plz
Coordinate System: LV95 (EPSG:2056)
"""

from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional


class PostalLocalityV1(BaseModel):
    """Swiss postal locality (Ortschaft) - Version 1.

    This model represents the canonical structure for Swiss postal localities
    as provided by swisstopo. The structure is stable and has been consistent
    since 2008.

    Data Source:
        ch.swisstopo-vd.ortschaftenverzeichnis_plz
        https://data.geo.admin.ch/

    Coordinate System:
        LV95 (EPSG:2056) - Swiss coordinate reference system

    Standards:
        - eCH-0010: Postal address standard
        - BFS municipality numbering

    Attributes:
        locality_name: Official locality name (e.g., "Zürich", "Genève")
        postal_code: 4-digit Swiss postal code (PLZ/NPA)
        additional_digit: 2-digit additional code for sub-localities (00 if none)
        municipality_name: Official municipality name
        bfs_number: BFS (Federal Statistical Office) municipality number
        canton_code: Two-letter canton abbreviation (e.g., "ZH", "GE")
        easting: Easting coordinate in LV95 system
        northing: Northing coordinate in LV95 system
        language: Primary language code (de, fr, it, rm)
        validity_date: Date from which this entry is valid (YYYY-MM-DD)

    Examples:
        >>> locality = PostalLocalityV1(
        ...     locality_name="Zürich",
        ...     postal_code="8001",
        ...     additional_digit="00",
        ...     municipality_name="Zürich",
        ...     bfs_number=261,
        ...     canton_code="ZH",
        ...     easting=2683141.0,
        ...     northing=1247935.0,
        ...     language="de",
        ...     validity_date="2008-07-01"
        ... )
        >>> locality.full_postal_code
        '8001'
        >>> locality.coordinates_lv95
        (2683141.0, 1247935.0)

    Version History:
        v1: Initial stable version
    """

    model_config = ConfigDict(
        frozen=True,              # Immutable - no field changes after creation
        strict=True,              # No type coercion
        str_strip_whitespace=True # Auto-strip whitespace from strings
    )

    # Core identification
    locality_name: str = Field(
        ...,
        description="Official locality name (Ortschaftsname)",
        min_length=1,
        max_length=100
    )

    postal_code: str = Field(
        ...,
        description="4-digit Swiss postal code (PLZ/NPA)",
        pattern=r'^\d{4}$'
    )

    additional_digit: str = Field(
        default="00",
        description="2-digit additional code for sub-localities (Zusatzziffer)",
        pattern=r'^\d{2}$'
    )

    # Administrative hierarchy
    municipality_name: str = Field(
        ...,
        description="Official municipality name (Gemeindename)",
        min_length=1,
        max_length=100
    )

    bfs_number: int = Field(
        ...,
        description="BFS (Federal Statistical Office) municipality number",
        ge=1,
        le=9999
    )

    canton_code: str = Field(
        ...,
        description="Two-letter canton abbreviation (Kantonskürzel), empty for Liechtenstein",
        pattern=r'^([A-Z]{2}|)$'
    )

    # Geographic coordinates (LV95)
    easting: float = Field(
        ...,
        description="Easting (E) coordinate in LV95 system",
        ge=2485000.0,
        le=2834000.0
    )

    northing: float = Field(
        ...,
        description="Northing (N) coordinate in LV95 system",
        ge=1075000.0,
        le=1296000.0
    )

    # Metadata
    language: str = Field(
        ...,
        description="Primary language code (de=German, fr=French, it=Italian, rm=Romansh, multiple=bilingual)",
        pattern=r'^(de|fr|it|rm|multiple)$'
    )

    validity_date: str = Field(
        ...,
        description="Date from which this entry is valid (YYYY-MM-DD format)",
        pattern=r'^\d{4}-\d{2}-\d{2}$'
    )

    @field_validator('canton_code', mode='before')
    @classmethod
    def uppercase_canton_code(cls, v: str) -> str:
        """Ensure canton code is uppercase, allow empty for Liechtenstein."""
        if v and v.strip():
            return v.upper().strip()
        return ''

    @property
    def full_postal_code(self) -> str:
        """Get full postal code including additional digit if not '00'.

        Returns:
            Postal code with additional digit if present (e.g., "8001-02"),
            otherwise just the postal code (e.g., "8001")

        Examples:
            >>> locality = PostalLocalityV1(postal_code="8001", additional_digit="00", ...)
            >>> locality.full_postal_code
            '8001'
            >>> locality = PostalLocalityV1(postal_code="8001", additional_digit="02", ...)
            >>> locality.full_postal_code
            '8001-02'
        """
        if self.additional_digit and self.additional_digit != "00":
            return f"{self.postal_code}-{self.additional_digit}"
        return self.postal_code

    @property
    def coordinates_lv95(self) -> tuple[float, float]:
        """Get coordinates as (easting, northing) tuple in LV95 system.

        Returns:
            Tuple of (easting, northing) coordinates

        Examples:
            >>> locality = PostalLocalityV1(easting=2683141.0, northing=1247935.0, ...)
            >>> locality.coordinates_lv95
            (2683141.0, 1247935.0)
        """
        return (self.easting, self.northing)

    def __str__(self) -> str:
        """String representation."""
        return f"{self.postal_code} {self.locality_name} ({self.canton_code})"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (
            f"PostalLocalityV1(postal_code='{self.postal_code}', "
            f"locality_name='{self.locality_name}', "
            f"bfs_number={self.bfs_number})"
        )


# Placeholder for future version if API changes
# class PostalLocalityV2(BaseModel):
#     """V2 model when/if API format changes significantly."""
#     pass
