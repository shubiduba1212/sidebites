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
            "- Accurately capture the emotional atmosphere (e.g., excitement, frustration, happiness, irony, regret)\n"
            "- Highlight subtle stylistic details such as lighting, background mood, facial expressions, clothing, and body language\n"
            "- Reflect the cultural nuance and playful tone of Korean slang while maintaining natural, vivid English expression\n"
            "- Maintain a cinematic, high-quality, and slightly exaggerated illustration style to suit dynamic comic scenes\n\n"
            "Examples:\n"
            "- For \"혼코노\" (solo coin karaoke room): Describe a joyful individual passionately singing alone in a brightly lit, neon-colored small booth, expressing freedom and happiness.\n"
            "- For \"지못미\" (sorry I couldn't protect you): Show a distraught fan who spent a fortune on idol merchandise, only to find the printed faces distorted, whispering \"My apologies to my bank account and my idols\" in a messy, poster-filled bedroom.\n"
            "- For \"웃프다\" (funny but sad): Depict an office worker laughing bitterly with tears in their eyes after discovering that their long-awaited bonus is only 5,000 won, under harsh fluorescent office lighting.\n"
            "- For \"갑분싸\" (sudden awkward silence): Portray a lively conversation abruptly halted after one person's heavy joke, leaving everyone frozen mid-laughter in awkward tension.\n"
            "- For \"사바사\" (case-by-case): Illustrate a food tasting event where people react completely differently to the same dish — some ecstatic, others grimacing — while an observer chuckles and remarks, \"Truly a matter of personal taste.\"\n\n"
            "Important:\n"
            "- If a Korean slang phrase has a strong emotional punch (e.g., \"킹받네\", \"이생망\", \"텅장\"), exaggerate the character's emotional expression to make it visually engaging.\n"
            "- Preserve unique Korean expressions like \"안물안궁\", \"문찐\", and others if possible, or translate them naturally while maintaining their cultural flavor.\n"
            "- For slang like \"갑분싸\", avoid depicting actual arguments or fights. Focus instead on emotional awkwardness, heavy silence, or social tension without escalation to conflict.\n\n"
            
            "Structure:\n"
            "- If the situation involves a progression of emotions or actions (e.g., joy → surprise → disappointment), divide the scene into 3–4 comic-style panels.\n"
            "- Focus finely on each emotional shift or action step as a distinct panel to enrich the storytelling.\n"
            "- Even short or simple situations can be expanded into multiple panels by zooming in on micro-emotions (such as laughter → realization → awkwardness).\n"
            "- Keep each panel visually distinct, enhancing the dynamic flow from one moment to the next."
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