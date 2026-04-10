from typing import Any

from .data_loader import LocalDatasetLoader
from .utils import paginate


class ObjectsService:
    def __init__(self, loader: LocalDatasetLoader | None = None) -> None:
        self.loader = loader or LocalDatasetLoader()

    def list_objects(
        self,
        name: str | None,
        object_type: str | None,
        constellation: str | None,
        page: int,
        page_size: int,
    ) -> dict[str, Any]:
        objects = self.loader.load_objects()
        filtered = [
            obj
            for obj in objects
            if self._matches(
                obj=obj,
                name=name,
                object_type=object_type,
                constellation=constellation,
            )
        ]
        return paginate(filtered, page=page, page_size=page_size)

    def get_by_id(self, object_id: int) -> dict[str, Any] | None:
        objects = self.loader.load_objects()
        for obj in objects:
            if obj.get("id") == object_id:
                return obj
        return None

    def _matches(
        self,
        obj: dict[str, Any],
        name: str | None,
        object_type: str | None,
        constellation: str | None,
    ) -> bool:
        obj_name = str(obj.get("name", "")).lower()
        obj_type = str(obj.get("object_type", "")).lower()
        obj_constellation = str(obj.get("constellation", "")).lower()

        if name and name.lower() not in obj_name:
            return False
        if object_type and object_type.lower() not in obj_type:
            return False
        if constellation and constellation.lower() not in obj_constellation:
            return False

        return True
