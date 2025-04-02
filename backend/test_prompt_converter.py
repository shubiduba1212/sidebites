# test_prompt_converter.py
from app.utils.prompt_converter import translate_and_style

def test_translate():
    korean_prompt = "혼자 노래방에서 노래 부르는 사람"
    english_prompt = translate_and_style(korean_prompt)
    print("🎯 변환된 프롬프트:")
    print(english_prompt)

if __name__ == "__main__":
    test_translate()
