from enum import Enum
from typing import Literal, Optional, Union

from pydantic import BaseModel, Field

from .objects import CelestialObject
from .stars import Star


class GuideCategory(str, Enum):
    star = "star"
    object = "object"


class UserLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class GuideExplainRequest(BaseModel):
    name: str = Field(..., min_length=1, examples=["Betelgeuse"])
    category: Optional[GuideCategory] = Field(default=None, examples=["star"])
    user_level: UserLevel = Field(default=UserLevel.beginner, examples=["beginner"])
    include_scientific_facts: bool = Field(default=True, examples=[True])
    context: Optional[str] = Field(default=None, examples=["User asked about red supergiants."])


class GuideExplainResponse(BaseModel):
    status: Literal["success"] = Field(default="success", examples=["success"])
    object_found: bool = Field(default=True, examples=[True])
    data: Union[Star, CelestialObject] = Field(...)
    explanation: str = Field(..., examples=["Betelgeuse is a red supergiant star in Orion."])
    key_facts: list[str] = Field(
        ...,
        examples=[
            [
                "Located in the constellation Orion",
                "A red supergiant star",
                "One of the brightest stars visible in the night sky",
            ]
        ],
    )


class GuideExplainNotFoundResponse(BaseModel):
    status: Literal["not_found"] = Field(default="not_found", examples=["not_found"])
    object_found: bool = Field(default=False, examples=[False])
    data: None = Field(default=None)
    explanation: str = Field(
        ...,
        examples=["No star or celestial object named 'Unknown Star' was found in the local dataset."],
    )
    key_facts: list[str] = Field(default_factory=list, examples=[[]])
