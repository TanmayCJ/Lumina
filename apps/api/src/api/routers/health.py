from fastapi import APIRouter

from ...core.config import get_settings
from ...models.health import HealthResponse

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    description="Returns service health status and API version.",
)
def get_health() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(status="ok", service="lumina-api", version=settings.api_version)
