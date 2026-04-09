from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    app_name: str = "Lumina Astronomy API"
    api_version: str = "1.0.0"
    data_dir: Path = Path(__file__).resolve().parent.parent / "data"


@lru_cache
def get_settings() -> Settings:
    return Settings()
