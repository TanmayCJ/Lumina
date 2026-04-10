import json
from pathlib import Path
from typing import Any

from ..core.config import get_settings


class LocalDatasetLoader:
    def __init__(self, data_dir: Path | None = None) -> None:
        settings = get_settings()
        self.data_dir = data_dir or settings.data_dir

    def load_stars(self) -> list[dict[str, Any]]:
        return self._load_dataset("stars.json", _fallback_stars())

    def load_objects(self) -> list[dict[str, Any]]:
        return self._load_dataset("objects.json", _fallback_objects())

    def load_exoplanets(self) -> list[dict[str, Any]]:
        return self._load_dataset("exoplanets.json", _fallback_exoplanets())

    def _load_dataset(self, filename: str, fallback_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        path = self.data_dir / filename
        if not path.exists():
            return fallback_data

        try:
            with path.open("r", encoding="utf-8") as fp:
                payload = json.load(fp)
                if isinstance(payload, list):
                    return payload
        except (OSError, json.JSONDecodeError):
            return fallback_data

        return fallback_data


def _fallback_stars() -> list[dict[str, Any]]:
    return [
        {
            "id": 1,
            "name": "Betelgeuse",
            "category": "star",
            "constellation": "Orion",
            "distance_light_years": 548.0,
            "magnitude": 0.42,
            "spectral_type": "M1-M2 Ia-ab",
            "description": "A red supergiant star in Orion.",
        }
    ]


def _fallback_objects() -> list[dict[str, Any]]:
    return [
        {
            "id": 101,
            "name": "Orion Nebula",
            "category": "object",
            "object_type": "nebula",
            "constellation": "Orion",
            "distance_light_years": 1344.0,
            "description": "A diffuse nebula and active star-forming region.",
        }
    ]


def _fallback_exoplanets() -> list[dict[str, Any]]:
    return [
        {
            "id": "exo-001",
            "name": "Kepler-186f",
            "host_star": "Kepler-186",
            "discovery_method": "Transit",
        }
    ]
