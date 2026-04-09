from typing import Any

from .data_loader import LocalDatasetLoader
from .utils import paginate


class StarsService:
    def __init__(self, loader: LocalDatasetLoader | None = None) -> None:
        self.loader = loader or LocalDatasetLoader()

    def list_stars(
        self,
        name: str | None,
        spectral_type: str | None,
        min_distance: float | None,
        max_distance: float | None,
        min_magnitude: float | None,
        max_magnitude: float | None,
        constellation: str | None,
        page: int,
        page_size: int,
    ) -> dict[str, Any]:
        stars = self.loader.load_stars()
        filtered = [
            s
            for s in stars
            if self._matches(
                star=s,
                name=name,
                spectral_type=spectral_type,
                min_distance=min_distance,
                max_distance=max_distance,
                min_magnitude=min_magnitude,
                max_magnitude=max_magnitude,
                constellation=constellation,
            )
        ]
        return paginate(filtered, page=page, page_size=page_size)

    def get_by_id(self, star_id: str) -> dict[str, Any] | None:
        stars = self.loader.load_stars()
        for star in stars:
            if star.get("id") == star_id:
                return star
        return None

    def _matches(
        self,
        star: dict[str, Any],
        name: str | None,
        spectral_type: str | None,
        min_distance: float | None,
        max_distance: float | None,
        min_magnitude: float | None,
        max_magnitude: float | None,
        constellation: str | None,
    ) -> bool:
        star_name = str(star.get("name", "")).lower()
        star_spectral = str(star.get("spectral_type", "")).lower()
        star_constellation = str(star.get("constellation", "")).lower()
        distance = star.get("distance_light_years")
        magnitude = star.get("apparent_magnitude")

        if name and name.lower() not in star_name:
            return False
        if spectral_type and spectral_type.lower() != star_spectral:
            return False
        if constellation and constellation.lower() != star_constellation:
            return False
        if min_distance is not None and (distance is None or distance < min_distance):
            return False
        if max_distance is not None and (distance is None or distance > max_distance):
            return False
        if min_magnitude is not None and (magnitude is None or magnitude < min_magnitude):
            return False
        if max_magnitude is not None and (magnitude is None or magnitude > max_magnitude):
            return False

        return True
