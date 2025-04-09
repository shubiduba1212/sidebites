# prompt_converter.py
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_and_style(korean_text: str) -> str:
    # ✅ 입력 유효성 검사
    if not korean_text or len(korean_text.strip()) < 2:
        return "Please provide a more meaningful slang term."
    
    """
    한글 시나리오 문장을 영어로 번역하고 스타일/분위기 요소를 추가하여
    이미지 생성용 프롬프트로 변환합니다.
    """
    system_prompt = (
        "You are a helpful assistant that converts Korean comic panel scenes into detailed English prompts for image generation using Stable Diffusion. "
        "Make the output descriptive, visually rich, and suitable for high-quality AI-generated illustrations."
    )

    user_prompt = f"Convert the following Korean comic panel description into an English prompt with a cinematic visual style:\n'{korean_text}'"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )

    return response.choices[0].message.content.strip()

# ✅ 테스트용 (직접 실행 시)
if __name__ == "__main__":
    example_kr = "노을지는 창가에서 혼자 노래하는 고양이"
    result = translate_and_style(example_kr)
    print("\n🎯 변환된 프롬프트:\n", result)

# def translate_and_style(prompt_kr: str) -> str:
#     """
#     한국어 문장을 Stable Diffusion용 영어 프롬프트로 번역하고 스타일을 추가합니다.
#     """
#     system_prompt = (
#         "You are a prompt engineer that translates Korean descriptions into English prompts "
#         "for Stable Diffusion image generation. Add details and artistic styles "
#         "like 'anime style', 'cinematic lighting', or 'detailed illustration'."
#     )

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": f"Translate and enhance this for Stable Diffusion: {prompt_kr}"}
#         ]
#     )

#     return response.choices[0].message.content.strip()