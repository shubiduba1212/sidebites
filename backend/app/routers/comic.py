from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import base64
import io
from PIL import Image
from ..services.scenario_generator import generate_scenario_from_slang
from ..utils.prompt_converter import translate_and_style
from ..services.image_generator import generate_images_from_prompts
from ..services.colab_client import COLAB_URL

router = APIRouter()

class PromptRequest(BaseModel):
  prompt : str

class ComicResponse(BaseModel):
    scenario: List[str]
    prompts: List[str]
    images: List[str]  # base64 인코딩된 이미지

@router.post("/generate", response_model=Dict)
def generate_comic(request: PromptRequest):
    try:
        slang = request.prompt

        # 1. 시나리오 생성
        scenario_lines: List[str] = generate_scenario_from_slang(slang)

        # 2. 각 시나리오 라인 → 프롬프트 변환
        prompts: List[str] = [translate_and_style(line) for line in scenario_lines]

        # 3. 프롬프트로 이미지 생성 (Colab 서버 연동)
        # image_urls: List[str] = generate_images_from_prompts(prompts, colab_url=COLAB_URL)
        images: List[Image.Image] = generate_images_from_prompts(prompts, COLAB_URL)

        # 4. 통합 응답 반환
        image_base64_list = []
        for img in images:
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            img_bytes = base64.b64encode(buf.getvalue()).decode("utf-8")
            image_base64_list.append(img_bytes)

        return ComicResponse(
            scenario=scenario_lines,
            prompts=prompts,
            images=image_base64_list
        )
        # return {
        #     "slang": slang,
        #     "scenario": scenario_lines,
        #     "prompts": prompts,
        #     "images": image_urls
        # }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# import requests
# from fastapi import APIRouter, Body, HTTPException
# from pydantic import BaseModel
# from typing import List
# from fastapi.responses import JSONResponse
# from ..utils.prompt_converter import translate_and_style
# from ..services.image_generator import generate_images_from_prompts
# from PIL import Image
# import io
# import base64
# # from ..services.generate_4panel import generate_4panel_mock
# # from ..services.colab_client import request_colab_images

# router = APIRouter()

# class PromptRequest(BaseModel):
#   prompt : str

# @router.post("/generate")
# def generate_comic_images(request: PromptRequest):
#   try:
#     # 1. 프롬프트 변환
#     english_prompt = translate_and_style(request.prompt)

#     # 2. 이미지 생성 요청 (Colab 서버 URL을 넣어야 함)
#     colab_url = "https://6b06-34-142-132-34.ngrok-free.app"
#     images: List[Image.Image] = generate_images_from_prompts([english_prompt]*4, colab_url)

#     # 3. 이미지 -> base64로 인코딩하여 반환
#     image_base64_list = []
#     for image in images:
#         buffered = io.BytesIO()
#         image.save(buffered, format="PNG")
#         img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
#         image_base64_list.append(img_str)
    
#     return {"images" : image_base64_list}

#   except Exception as e:
#      raise HTTPException(status_code=500, detail=str(e))

# FLASK_SERVER_URL = "https://6b06-34-142-132-34.ngrok-free.app/generate"

# @router.post("/generate")
# def generate_full_comic(slang : str) :
#     scenario = generate_scenario_from_slang(slang)
#     prompts = convert_scenario_to_prompts(scenario)
#     image_urls = generate_images_from_prompts(prompts)

#     return {"scenario" : scenario, "prompts" : prompts, "image_urls" : image_urls}

    # 1. 시나리오 생성
    # scenario_lines = generate_scenario(slang)

    # # 2. 각 줄을 스타일링
    # prompts = [translate_and_style(line) for line in scenario_lines]

    # # 3. Colab 서버에 요청 (이미지 생성)
    # image_urls = post_to_colab(prompts)

    # # 4. 최종 응답
    # return {"slang" : slang, "scenario" : scenario_lines, "image_urls" : image_urls}

# @router.post("/test-colab")
# def test_colab_intergration(prompt : str = Body(..., embed=True)):
#   try:
#       response = requests.post(FLASK_SERVER_URL, json={"prompt" : prompt})
#       response.raise_for_status()
#       return JSONResponse(content=response.json())
#   except Exception as e:
#      return JSONResponse(status_code=500, content={"error" : str(e)})

# @router.post("/generate")
# def generate_comic_images(prompt : str) :
#   response = requests.post(
#       "https://xxxxx.ngrok.io/generate",  # 위에서 받은 주소로 교체!
#       json={"prompt": prompt}
#   )
#   return response.json().get("images", [])
  # """
  # 하나의 프롬프트로 4컷 만화 이미지를 생성하는 엔드포인트
  # """
  # image_urls = request_colab_images(prompt)
  # return {"image_urls" : image_urls}

# def generate_comic(prompt : str = Body(..., embed=True)) :
#   image_url = generate_comic_image(prompt)
#   if image_url :
#     return{"image_url" : image_url}
#   return {"error" : "이미지 생성 실패"}

# @router.get("/generate-comic") 
# def generate_comic_prompt(query: str = Query(..., description="줄임말")):
#   example_meaning = "혼자 코인노래방 가는 것" #테스트용
#   prompt = build_comic_prompt(query, example_meaning)
#   return {"prompt" : prompt}