from typing import List
from PIL import Image
import requests
import io

def generate_images_from_prompts(prompts: List[str], colab_url:str) -> List[Image.Image]:
  """
  전달된 각 프롬프트에 대해 이미지 생성 요청을 보내고 결과 이미지를 리스트로 반환합니다.
  """
  response = requests.post(f"{colab_url}/generate", json={"prompts" : prompts})
  if response.status_code != 200:
    raise RuntimeError(f"이미지 생성 실패 : {response.text}")
  
  image_urls = response.json().get("images", [])
  images = []
  for url in image_urls:
    img_response = requests.get(url)
    if img_response.status_code == 200:
      images.append(Image.open(io.BytesIO(img_response)))
    else:
      print(f"❌ 이미지 다운로드 실패: {url}")
  return images