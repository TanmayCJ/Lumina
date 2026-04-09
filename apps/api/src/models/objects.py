from typing import Optional

from pydantic import BaseModel, Field

from .common import PaginationMeta


class CelestialObject(BaseModel):
    id: str = Field(..., examples=["obj-001"])
    name: str = Field(..., examples=["Orion Nebula"])
    object_type: str = Field(..., examples=["nebula"])
    constellation: Optional[str] = Field(default=None, examples=["Orion"])
    distance_light_years: Optional[float] = Field(default=None, ge=0, examples=[1344.0])
    description: Optional[str] = Field(default=None, examples=["A diffuse nebula south of Orion's Belt."])


class ObjectSearchRequest(BaseModel):
    name: Optional[str] = Field(default=None, examples=["orion"])
    object_type: Optional[str] = Field(default=None, examples=["nebula"])
    constellation: Optional[str] = Field(default=None, examples=["Orion"])
    page: int = Field(default=1, ge=1, examples=[1])
    page_size: int = Field(default=10, ge=1, le=100, examples=[10])


class ObjectListResponse(BaseModel):
    items: list[CelestialObject]
    pagination: PaginationMeta


class ObjectDetailResponse(BaseModel):
    item: CelestialObject
