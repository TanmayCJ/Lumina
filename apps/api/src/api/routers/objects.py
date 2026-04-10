from fastapi import APIRouter, Query

from ...core.exceptions import DatasetEntityNotFound
from ...models.objects import ObjectDetailResponse, ObjectListResponse, ObjectSearchRequest
from ...services.objects_service import ObjectsService

router = APIRouter(prefix="/api/v1/objects", tags=["Objects"])
service = ObjectsService()


@router.get(
    "",
    response_model=ObjectListResponse,
    summary="List Celestial Objects",
    description="List celestial objects with filters by name, object type, and constellation.",
)
def list_objects(
    name: str | None = Query(default=None),
    object_type: str | None = Query(default=None),
    constellation: str | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
) -> ObjectListResponse:
    result = service.list_objects(
        name=name,
        object_type=object_type,
        constellation=constellation,
        page=page,
        page_size=page_size,
    )
    return ObjectListResponse(**result)


@router.get(
    "/{object_id}",
    response_model=ObjectDetailResponse,
    summary="Get Celestial Object by ID",
    description="Fetch a single celestial object record by unique object id.",
)
def get_object_by_id(object_id: int) -> ObjectDetailResponse:
    item = service.get_by_id(object_id)
    if item is None:
        raise DatasetEntityNotFound("Object", str(object_id))
    return ObjectDetailResponse(item=item)


@router.post(
    "/search",
    response_model=ObjectListResponse,
    summary="Search Celestial Objects",
    description="Search celestial objects with a JSON request body.",
)
def search_objects(payload: ObjectSearchRequest) -> ObjectListResponse:
    result = service.list_objects(
        name=payload.name,
        object_type=payload.object_type,
        constellation=payload.constellation,
        page=payload.page,
        page_size=payload.page_size,
    )
    return ObjectListResponse(**result)
