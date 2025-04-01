from fastapi import APIRouter, Body
from ..services.prompt_builder import generate_comic_image

router = APIRouter()

@router.post("/generate")
def generate_comic(prompt : str = Body(..., embed=True)) :
  image_url = generate_comic_image(prompt)
  if image_url :
    return{"image_url" : image_url}
  return {"error" : "이미지 생성 실패"}

# @router.get("/generate-comic") 
# def generate_comic_prompt(query: str = Query(..., description="줄임말")):
#   example_meaning = "혼자 코인노래방 가는 것" #테스트용
#   prompt = build_comic_prompt(query, example_meaning)
#   return {"prompt" : prompt}