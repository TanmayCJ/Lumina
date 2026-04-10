from fastapi import APIRouter, Query

from ...core.exceptions import DatasetEntityNotFound
from ...models.stars import StarDetailResponse, StarListResponse, StarSearchRequest
from ...services.stars_service import StarsService

router = APIRouter(prefix="/api/v1/stars", tags=["Stars"])
service = StarsService()


@router.get(
    "",
    response_model=StarListResponse,
    summary="List Stars",
    description="List stars with optional filters for name, spectral class, distance, magnitude, and constellation.",
)
def list_stars(
    name: str | None = Query(default=None),
    spectral_type: str | None = Query(default=None),
    min_distance: float | None = Query(default=None, ge=0),
    max_distance: float | None = Query(default=None, ge=0),
    min_magnitude: float | None = Query(default=None),
    max_magnitude: float | None = Query(default=None),
    constellation: str | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
) -> StarListResponse:
    result = service.list_stars(
        name=name,
        spectral_type=spectral_type,
        min_distance=min_distance,
        max_distance=max_distance,
        min_magnitude=min_magnitude,
        max_magnitude=max_magnitude,
        constellation=constellation,
        page=page,
        page_size=page_size,
    )
    return StarListResponse(**result)


@router.get(
    "/{star_id}",
    response_model=StarDetailResponse,
    summary="Get Star by ID",
    description="Fetch a single star record by unique star id.",
)
def get_star_by_id(star_id: int) -> StarDetailResponse:
    item = service.get_by_id(star_id)
    if item is None:
        raise DatasetEntityNotFound("Star", str(star_id))
    return StarDetailResponse(item=item)


@router.post(
    "/search",
    response_model=StarListResponse,
    summary="Search Stars",
    description="Search stars with a JSON request body. Useful for complex filters from frontend clients.",
)
def search_stars(payload: StarSearchRequest) -> StarListResponse:
    result = service.list_stars(
        name=payload.name,
        spectral_type=payload.spectral_type,
        min_distance=payload.min_distance,
        max_distance=payload.max_distance,
        min_magnitude=payload.min_magnitude,
        max_magnitude=payload.max_magnitude,
        constellation=payload.constellation,
        page=payload.page,
        page_size=payload.page_size,
    )
    return StarListResponse(**result)
