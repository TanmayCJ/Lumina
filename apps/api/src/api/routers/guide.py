from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ...models.guide import GuideExplainNotFoundResponse, GuideExplainRequest, GuideExplainResponse
from ...services.guide_service import GuideService

router = APIRouter(prefix="/api/v1/guide", tags=["Guide"])
service = GuideService()


@router.post(
    "/explain",
    response_model=GuideExplainResponse,
    responses={404: {"model": GuideExplainNotFoundResponse}},
    summary="Generate Guided Explanation",
    description=(
        "Generate a guided educational explanation for a star or celestial object. "
        "If category is omitted, Lumina auto-detects from local curated datasets."
    ),
)
def explain(payload: GuideExplainRequest) -> GuideExplainResponse | JSONResponse:
    result = service.explain(payload)
    if result is None:
        return JSONResponse(
            status_code=404,
            content={
                "status": "not_found",
                "object_found": False,
                "data": None,
                "explanation": (
                    f"No star or celestial object named '{payload.name}' was found in the local dataset."
                ),
                "key_facts": [],
            },
        )
    return result
