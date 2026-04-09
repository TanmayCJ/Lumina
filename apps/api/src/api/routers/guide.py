from fastapi import APIRouter

from ...models.guide import GuideExplainRequest, GuideExplainResponse
from ...services.guide_service import GuideService

router = APIRouter(prefix="/api/v1/guide", tags=["Guide"])
service = GuideService()


@router.post(
    "/explain",
    response_model=GuideExplainResponse,
    summary="Generate Guided Explanation",
    description=(
        "Generate an educational response structure for a requested astronomy topic. "
        "Current implementation uses local dataset context and deterministic placeholder logic."
    ),
)
def explain(payload: GuideExplainRequest) -> GuideExplainResponse:
    return service.explain(payload)
