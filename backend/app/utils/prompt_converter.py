# prompt_converter.py
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_and_style(prompt_kr: str) -> str:
    """
    한국어 문장을 Stable Diffusion용 영어 프롬프트로 번역하고 스타일을 추가합니다.
    """
    system_prompt = (
        "You are a prompt engineer that translates Korean descriptions into English prompts "
        "for Stable Diffusion image generation. Add details and artistic styles "
        "like 'anime style', 'cinematic lighting', or 'detailed illustration'."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Translate and enhance this for Stable Diffusion: {prompt_kr}"}
        ]
    )

    return response.choices[0].message.content.strip()