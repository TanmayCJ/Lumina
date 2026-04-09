from pydantic import BaseModel, Field


class PaginationMeta(BaseModel):
    page: int = Field(..., ge=1, examples=[1])
    page_size: int = Field(..., ge=1, le=100, examples=[10])
    total_items: int = Field(..., ge=0, examples=[125])
    total_pages: int = Field(..., ge=0, examples=[13])
