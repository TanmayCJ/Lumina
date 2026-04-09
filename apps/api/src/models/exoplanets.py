from typing import Optional

from pydantic import BaseModel, Field

from .common import PaginationMeta


class Exoplanet(BaseModel):
    id: str = Field(..., examples=["exo-001"])
    name: str = Field(..., examples=["Kepler-186f"])
    host_star: str = Field(..., examples=["Kepler-186"])
    discovery_method: str = Field(..., examples=["Transit"])
    discovery_year: Optional[int] = Field(default=None, ge=0, examples=[2014])
    distance_light_years: Optional[float] = Field(default=None, ge=0, examples=[492.0])
    orbital_period_days: Optional[float] = Field(default=None, ge=0, examples=[129.9])
    radius_earth: Optional[float] = Field(default=None, ge=0, examples=[1.11])
    mass_jupiter: Optional[float] = Field(default=None, ge=0, examples=[0.01])
    potentially_habitable: Optional[bool] = Field(default=None, examples=[True])
    constellation: Optional[str] = Field(default=None, examples=["Cygnus"])
    summary: Optional[str] = Field(default=None, examples=["A potentially rocky exoplanet in the habitable zone."])


class ExoplanetSearchRequest(BaseModel):
    name: Optional[str] = Field(default=None, examples=["kepler"])
    host_star: Optional[str] = Field(default=None, examples=["Kepler-186"])
    discovery_method: Optional[str] = Field(default=None, examples=["Transit"])
    page: int = Field(default=1, ge=1, examples=[1])
    page_size: int = Field(default=10, ge=1, le=100, examples=[10])


class ExoplanetListResponse(BaseModel):
    items: list[Exoplanet]
    pagination: PaginationMeta


class ExoplanetDetailResponse(BaseModel):
    item: Exoplanet
