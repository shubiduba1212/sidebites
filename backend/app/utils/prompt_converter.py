# prompt_converter.py
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def log_prompt_process(step: str, content: str):
    print(f"[{step}] {content}")

def translate_and_style(korean_text: str) -> str:
    # ✅ 입력 유효성 검사
    if not korean_text or len(korean_text.strip()) < 2:
        return "Please provide a more meaningful slang term."
    
    log_prompt_process("🔍 입력된 문장", korean_text)
    
    """
    한글 시나리오 문장을 영어로 번역하고 스타일/분위기 요소를 추가하여
    이미지 생성용 프롬프트로 변환합니다.

    ✅ 개선 아이디어 메모
    - 변환할 때 조명(lighting), 분위기(atmosphere), 감정(emotion) 요소를 더 강조해줄 것
    - Make sure to emphasize subtle, thoughtful touches that showcase the character's wit, sense, and attention to atmosphere.
    """
    try:
        system_prompt = (
            "You are a highly creative assistant that transforms Korean slang-based comic panel descriptions into detailed, emotionally expressive, and visually rich English prompts for AI image generation (e.g., Stable Diffusion).\n\n"
            "When generating prompts, make sure to:\n"
            "- Accurately capture the emotional atmosphere (e.g., excitement, frustration, awkwardness, irony, regret)\n"
            "- Highlight subtle stylistic details such as lighting, background mood, facial expressions, clothing, and body language\n"
            "- Reflect the cultural nuance and playful tone of Korean slang while maintaining natural, vivid English expression\n"
            "- Maintain a cinematic, high-quality, and slightly exaggerated illustration style suitable for dynamic comic scenes\n"
            "- Each panel must naturally progress, with a clear shift in emotion or situation per panel.\n\n"
            "Important guidelines:\n"
            "- Create between 2 to 4 panels depending on the story flow, but NEVER exceed 4 panels.\n"
            "- If the slang describes an emotional reversal (e.g., 갑분싸), the FINAL panel MUST clearly depict the emotional reversal (e.g., sudden awkward silence).\n"
            "- Ensure the final tone matches the essence of the slang (e.g., 갑분싸: awkwardness, not continued laughter).\n"
            "- Use environmental and character details (e.g., body stiffening, avoiding eye contact, strained smiles) to show the emotional shift.\n"
            "- Focus on vivid emotional storytelling through micro-expressions and atmosphere.\n\n"
            "Examples:\n"
            "- \"혼코노\": Joyful, triumphant singing in a neon-lit solo karaoke room.\n"
            "- \"지못미\": Deep regret in a cluttered, melancholic fan room.\n"
            "- \"갑분싸\": Start with lively chatter → shift to heavy, oppressive silence after a joke.\n"
            "- \"사바사\": Different emotional reactions to the same event.\n\n"
            "Structure:\n"
            "- 2 to 4 panels maximum.\n"
            "- Each panel must represent a distinct emotional or visual change.\n"
            "- Panels must stay visually descriptive and emotionally vivid.\n\n"
            "Tone:\n"
            "- Emotionally immersive, slightly playful but precise.\n"
            "- Strong visual storytelling fit for AI-driven illustration.\n"
        )

        user_prompt = f"Convert the following Korean comic panel description into an English prompt with a cinematic visual style:\n'{korean_text}'"

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )

        result = response.choices[0].message.content.strip()
        log_prompt_process("✅ 변환된 프롬프트", result)
        print(f"[✅ 변환된 프롬프트] {result}")  # ✅ 이 줄 추가
        return result

    except Exception as e:
        log_prompt_process("❌ 변환 실패", str(e))
        return "An error occurred while generating the prompt. Please try again later."

# ✅ 테스트용 (직접 실행 시)
if __name__ == "__main__":
    example_kr = '친구들끼리 신나게 웃고 떠들던 중, 한 명이 무거운 농담을 던져 갑자기 정적이 흐르는 장면'
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