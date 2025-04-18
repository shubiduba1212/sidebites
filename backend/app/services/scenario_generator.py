from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def generate_scenario_from_slang(slang : str) -> List[str]:
  if slang == "갑분싸":
        return [
            "친구들끼리 카페에서 신나게 웃고 떠드는 장면",
            "한 친구가 무거운 농담을 던지며 분위기를 살짝 깨는 장면",
            "모두가 순간 말문이 막히고 어색한 정적이 흐르는 장면",
            "사람들이 시선을 피하거나 애써 웃으려 하지만, 여전히 어색한 분위기가 감도는 장면"
        ]
  else:
    """
    줄임말(slang)을 입력받아 4컷 만화용 시나리오 4줄을 생성합니다.
    """

    system_prompt = (
      "사용자에게서 줄임말을 입력받으면, 그 줄임말의 의미를 상황극처럼 보여주는 이야기 4줄을 만들어줘.\n"
          "각 문장은 컷툰의 한 장면이 되므로, 구체적인 시각적 요소와 인물의 행동이 묘사되어야 해.\n"
          "예: '혼코노' ➝ ['고양이 한 마리가 혼자 노래방에 들어선다.', '마이크를 잡고 신나게 노래를 부르기 시작한다.', ...]"
    )

    user_prompt = f"줄임말: {slang}"

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content" : user_prompt}
      ],
      temperature=0.8
    )

    scenario_text = response.choices[0].message.content.strip()
    scenario_lines = [line.strip("- ").strip() for line in scenario_text.split("\n") if line.strip()]

    return scenario_lines[:4] #4줄만 반환