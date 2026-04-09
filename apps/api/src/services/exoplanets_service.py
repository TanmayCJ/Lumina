from typing import Any

from .data_loader import LocalDatasetLoader
from .utils import paginate


class ExoplanetsService:
    def __init__(self, loader: LocalDatasetLoader | None = None) -> None:
        self.loader = loader or LocalDatasetLoader()

    def list_exoplanets(
        self,
        name: str | None,
        host_star: str | None,
        discovery_method: str | None,
        page: int,
        page_size: int,
    ) -> dict[str, Any]:
        planets = self.loader.load_exoplanets()
        filtered = [
            p
            for p in planets
            if self._matches(
                planet=p,
                name=name,
                host_star=host_star,
                discovery_method=discovery_method,
            )
        ]
        return paginate(filtered, page=page, page_size=page_size)

    def get_by_id(self, planet_id: str) -> dict[str, Any] | None:
        planets = self.loader.load_exoplanets()
        for planet in planets:
            if planet.get("id") == planet_id:
                return planet
        return None

    def _matches(
        self,
        planet: dict[str, Any],
        name: str | None,
        host_star: str | None,
        discovery_method: str | None,
    ) -> bool:
        planet_name = str(planet.get("name", "")).lower()
        planet_host = str(planet.get("host_star", "")).lower()
        planet_method = str(planet.get("discovery_method", "")).lower()

        if name and name.lower() not in planet_name:
            return False
        if host_star and host_star.lower() not in planet_host:
            return False
        if discovery_method and discovery_method.lower() != planet_method:
            return False

        return True
