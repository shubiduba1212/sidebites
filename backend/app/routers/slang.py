from fastapi import APIRouter, Query
from app.services.slang_mapper import find_slang

router = APIRouter()

@router.get("/slang")
def get_slang(query: str = Query(..., description="검색할 한국 슬랭")):
    result = find_slang(query)
    return result
