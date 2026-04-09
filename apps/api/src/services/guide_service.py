from .data_loader import LocalDatasetLoader
from ..models.guide import GuideCategory, GuideExplainRequest, GuideExplainResponse, UserLevel


class GuideService:
    def __init__(self, loader: LocalDatasetLoader | None = None) -> None:
        self.loader = loader or LocalDatasetLoader()

    def explain(self, payload: GuideExplainRequest) -> GuideExplainResponse:
        related = self._find_related(payload.name, payload.category)
        overview = self._build_overview(payload.name, payload.category, payload.user_level)
        key_facts = self._build_key_facts(payload.name, payload.category, related)

        scientific_context = None
        if payload.include_scientific_facts:
            scientific_context = (
                "This summary references local catalog metadata and is designed for educational "
                "orientation before deeper scientific analysis."
            )

        return GuideExplainResponse(
            topic=payload.name,
            category=payload.category,
            user_level=payload.user_level,
            overview=overview,
            key_facts=key_facts,
            scientific_context=scientific_context,
            related_entities=related,
        )

    def _build_overview(self, name: str, category: GuideCategory, user_level: UserLevel) -> str:
        level_phrase = {
            UserLevel.beginner: "easy to follow",
            UserLevel.intermediate: "balanced between intuition and detail",
            UserLevel.advanced: "technical and concept-dense",
        }[user_level]
        return (
            f"{name} is treated as a {category.value} topic in Lumina's sky guide. "
            f"This explanation is {level_phrase} and organized for step-by-step learning."
        )

    def _build_key_facts(self, name: str, category: GuideCategory, related: list[str]) -> list[str]:
        facts = [
            f"{name} is indexed in Lumina's local {category.value} dataset.",
            "Filtering and search endpoints can retrieve this topic by name and attributes.",
            "Use constellation and classification metadata to connect related sky objects.",
        ]
        if related:
            facts.append(f"Related entries include: {', '.join(related[:3])}.")
        return facts

    def _find_related(self, name: str, category: GuideCategory) -> list[str]:
        name_lc = name.lower()

        if category == GuideCategory.star:
            stars = self.loader.load_stars()
            return [s.get("name", "") for s in stars if name_lc not in str(s.get("name", "")).lower()][:5]

        if category == GuideCategory.object:
            objects = self.loader.load_objects()
            return [o.get("name", "") for o in objects if name_lc not in str(o.get("name", "")).lower()][:5]

        if category == GuideCategory.exoplanet:
            planets = self.loader.load_exoplanets()
            return [p.get("name", "") for p in planets if name_lc not in str(p.get("name", "")).lower()][:5]

        if category == GuideCategory.constellation:
            stars = self.loader.load_stars()
            objects = self.loader.load_objects()
            related = [
                s.get("name", "")
                for s in stars
                if name_lc == str(s.get("constellation", "")).lower()
            ]
            related.extend(
                [
                    o.get("name", "")
                    for o in objects
                    if name_lc == str(o.get("constellation", "")).lower()
                ]
            )
            return related[:5]

        return []
