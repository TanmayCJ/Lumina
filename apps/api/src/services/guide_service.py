from typing import Any

from .data_loader import LocalDatasetLoader
from ..models.guide import GuideCategory, GuideExplainRequest, GuideExplainResponse, UserLevel


class GuideService:
    def __init__(self, loader: LocalDatasetLoader | None = None) -> None:
        self.loader = loader or LocalDatasetLoader()

    def explain(self, payload: GuideExplainRequest) -> GuideExplainResponse | None:
        matched = self._find_record(payload.name, payload.category)
        if matched is None:
            return None

        category, data = matched
        explanation = self._build_explanation(
            data=data,
            category=category,
            user_level=payload.user_level,
            include_scientific_facts=payload.include_scientific_facts,
        )
        key_facts = self._build_key_facts(data=data, category=category)

        return GuideExplainResponse(
            status="success",
            object_found=True,
            data=data,
            explanation=explanation,
            key_facts=key_facts,
        )

    def _find_record(
        self,
        name: str,
        category: GuideCategory | None,
    ) -> tuple[GuideCategory, dict[str, Any]] | None:
        name_lc = name.strip().lower()

        if category in (None, GuideCategory.star):
            for star in self.loader.load_stars():
                if name_lc == str(star.get("name", "")).lower():
                    return GuideCategory.star, star

        if category in (None, GuideCategory.object):
            for obj in self.loader.load_objects():
                if name_lc == str(obj.get("name", "")).lower():
                    return GuideCategory.object, obj

        return None

    def _build_explanation(
        self,
        data: dict[str, Any],
        category: GuideCategory,
        user_level: UserLevel,
        include_scientific_facts: bool,
    ) -> str:
        name = data.get("name", "This object")
        constellation = data.get("constellation", "its region of the sky")
        description = data.get("description", "a noteworthy astronomy target")
        distance = data.get("distance_light_years")

        if user_level == UserLevel.beginner:
            text = (
                f"{name} is {description.lower()} in {constellation}. "
                f"For a beginner, think of it as an easy anchor point to understand how different "
                f"types of {category.value}s appear in the night sky."
            )
        elif user_level == UserLevel.intermediate:
            text = (
                f"{name} is categorized as a {category.value} associated with {constellation}. "
                f"It helps connect sky-position learning with physical characteristics like brightness, "
                f"spectral class, and distance."
            )
        else:
            text = (
                f"{name} is modeled in the local catalog as a {category.value} in {constellation}. "
                f"Use this record as an entry point for comparative analysis of luminosity proxies, "
                f"classification, and astrophysical evolution context."
            )

        if include_scientific_facts and distance is not None:
            text += f" Current dataset distance estimate is approximately {distance} light-years."

        return text

    def _build_key_facts(self, data: dict[str, Any], category: GuideCategory) -> list[str]:
        facts: list[str] = []
        constellation = data.get("constellation")
        if constellation:
            facts.append(f"Located in the constellation {constellation}")

        if category == GuideCategory.star:
            spectral = data.get("spectral_type")
            if spectral:
                facts.append(f"Spectral type: {spectral}")
            facts.append("Cataloged as a star in Lumina's curated local dataset")
        else:
            obj_type = data.get("object_type")
            if obj_type:
                facts.append(f"Object type: {obj_type}")
            facts.append("Cataloged as a deep-sky object in Lumina's curated local dataset")

        distance = data.get("distance_light_years")
        if distance is not None:
            facts.append(f"Distance estimate: {distance} light-years")

        return facts
