from fastapi import APIRouter, Query

from ...core.exceptions import DatasetEntityNotFound
from ...models.exoplanets import ExoplanetDetailResponse, ExoplanetListResponse, ExoplanetSearchRequest
from ...services.exoplanets_service import ExoplanetsService

router = APIRouter(prefix="/api/v1/exoplanets", tags=["Exoplanets"])
service = ExoplanetsService()


@router.get(
    "",
    response_model=ExoplanetListResponse,
    summary="List Exoplanets",
    description="List exoplanets filtered by name, host star, or discovery method.",
)
def list_exoplanets(
    name: str | None = Query(default=None),
    host_star: str | None = Query(default=None),
    discovery_method: str | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
) -> ExoplanetListResponse:
    result = service.list_exoplanets(
        name=name,
        host_star=host_star,
        discovery_method=discovery_method,
        page=page,
        page_size=page_size,
    )
    return ExoplanetListResponse(**result)


@router.get(
    "/{planet_id}",
    response_model=ExoplanetDetailResponse,
    summary="Get Exoplanet by ID",
    description="Fetch one exoplanet by unique id.",
)
def get_exoplanet_by_id(planet_id: str) -> ExoplanetDetailResponse:
    item = service.get_by_id(planet_id)
    if item is None:
        raise DatasetEntityNotFound("Exoplanet", planet_id)
    return ExoplanetDetailResponse(item=item)


@router.post(
    "/search",
    response_model=ExoplanetListResponse,
    summary="Search Exoplanets",
    description="Search exoplanets with a JSON request body for structured filters.",
)
def search_exoplanets(payload: ExoplanetSearchRequest) -> ExoplanetListResponse:
    result = service.list_exoplanets(
        name=payload.name,
        host_star=payload.host_star,
        discovery_method=payload.discovery_method,
        page=payload.page,
        page_size=payload.page_size,
    )
    return ExoplanetListResponse(**result)
