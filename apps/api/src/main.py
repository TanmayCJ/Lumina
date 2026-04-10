from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .api.routers import guide, health, objects, stars
from .core.config import get_settings
from .core.exceptions import DatasetEntityNotFound


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version,
        summary="Milestone 1 backend for Lumina astronomy guide",
        description=(
            "Lumina API provides curated dataset endpoints for stars and celestial objects, "
            "plus a guided explanation endpoint designed for first product milestone validation."
        ),
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    @app.exception_handler(DatasetEntityNotFound)
    async def not_found_handler(_: Request, exc: DatasetEntityNotFound) -> JSONResponse:
        return JSONResponse(
            status_code=404,
            content={
                "error": "not_found",
                "message": str(exc),
            },
        )

    app.include_router(health.router)
    app.include_router(stars.router)
    app.include_router(objects.router)
    app.include_router(guide.router)

    return app


app = create_app()
