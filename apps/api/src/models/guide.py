from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class GuideCategory(str, Enum):
    star = "star"
    object = "object"
    exoplanet = "exoplanet"
    constellation = "constellation"
    general = "general"


class UserLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class GuideExplainRequest(BaseModel):
    name: str = Field(..., min_length=1, examples=["Betelgeuse"])
    category: GuideCategory = Field(..., examples=["star"])
    user_level: UserLevel = Field(default=UserLevel.beginner, examples=["beginner"])
    include_scientific_facts: bool = Field(default=True, examples=[True])
    context: Optional[str] = Field(default=None, examples=["User asked about red supergiants."])


class GuideExplainResponse(BaseModel):
    topic: str = Field(..., examples=["Betelgeuse"])
    category: GuideCategory = Field(..., examples=["star"])
    user_level: UserLevel = Field(..., examples=["beginner"])
    overview: str = Field(..., examples=["Betelgeuse is a red supergiant star in Orion."])
    key_facts: list[str] = Field(
        ...,
        examples=[
            [
                "Located in the constellation Orion",
                "A late-stage massive star",
                "Visible to the naked eye",
            ]
        ],
    )
    scientific_context: Optional[str] = Field(
        default=None,
        examples=["Its variability and size make it a key object in stellar evolution studies."],
    )
    related_entities: list[str] = Field(default_factory=list, examples=[["Rigel", "Orion Nebula"]])
    disclaimer: str = Field(
        default="Educational summary generated from local dataset placeholders.",
        examples=["Educational summary generated from local dataset placeholders."],
    )
