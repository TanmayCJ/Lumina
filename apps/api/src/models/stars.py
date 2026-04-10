from typing import Optional

from pydantic import BaseModel, Field

from .common import PaginationMeta


class Star(BaseModel):
    id: int = Field(..., examples=[2])
    name: str = Field(..., examples=["Betelgeuse"])
    category: str = Field(default="star", examples=["star"])
    constellation: Optional[str] = Field(default=None, examples=["Orion"])
    distance_light_years: float = Field(..., ge=0, examples=[548.0])
    magnitude: float = Field(..., examples=[0.42])
    spectral_type: str = Field(..., examples=["M1-M2 Ia-ab"])
    description: Optional[str] = Field(default=None, examples=["A red supergiant nearing end-of-life stages."])


class StarSearchRequest(BaseModel):
    name: Optional[str] = Field(default=None, examples=["Sirius"])
    spectral_type: Optional[str] = Field(default=None, examples=["A1V"])
    min_distance: Optional[float] = Field(default=None, ge=0, examples=[1.0])
    max_distance: Optional[float] = Field(default=None, ge=0, examples=[600.0])
    min_magnitude: Optional[float] = Field(default=None, examples=[-1.5])
    max_magnitude: Optional[float] = Field(default=None, examples=[1.0])
    constellation: Optional[str] = Field(default=None, examples=["Canis Major"])
    page: int = Field(default=1, ge=1, examples=[1])
    page_size: int = Field(default=10, ge=1, le=100, examples=[10])


class StarListResponse(BaseModel):
    items: list[Star]
    pagination: PaginationMeta


class StarDetailResponse(BaseModel):
    item: Star
