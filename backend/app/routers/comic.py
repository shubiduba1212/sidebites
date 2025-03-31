from fastapi import APIRouter, Query
from ..services.prompt_builder import build_comic_prompt

router = APIRouter()

@router.get("/generate-comic") 
def generate_comic_prompt(query: str = Query(..., description="줄임말")):
  example_meaning = "혼자 코인노래방 가는 것" #테스트용
  prompt = build_comic_prompt(query, example_meaning)
  return {"prompt" : prompt}