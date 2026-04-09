from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(..., examples=["ok"])
    service: str = Field(..., examples=["lumina-api"])
    version: str = Field(..., examples=["1.0.0"])
