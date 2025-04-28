from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def generate_scenario_from_slang(slang : str) -> List[str]:
  """
  줄임말을 기반으로 4줄 시나리오를 생성하는 함수.
  OpenAI를 호출해 JSON 배열로 정확하게 반환받는다.
  """
  print("[백엔드] generate_scenario_from_slang 호출됨. slang:", slang)
  if slang == "갑분싸":
        return [
            "친구들끼리 카페에서 신나게 웃고 떠드는 장면",
            "한 친구가 무거운 농담을 던지며 분위기를 살짝 깨는 장면",
            "모두가 순간 말문이 막히고 어색한 정적이 흐르는 장면",
            "사람들이 시선을 피하거나 애써 웃으려 하지만, 여전히 어색한 분위기가 감도는 장면"
        ]
  else:
    
    system_prompt = (      
      "너는 창의적인 스토리텔러야.\n"
      "사용자가 입력한 줄임말을 주제로 짧고 생동감 있는 4줄 스토리를 만들어야 해.\n"
      "반드시 JSON 배열로만 출력해. 추가 설명이나 텍스트 없이 배열만 보여줘.\n\n"
      "예시:\n"
      "[\"첫 번째 문장\", \"두 번째 문장\", \"세 번째 문장\", \"네 번째 문장\"]\n"
    )

    user_prompt = f"줄임말: {slang}\n이 줄임말을 주제로 4줄 스토리를 만들어줘. 출력은 반드시 JSON 배열로 해줘."

    try:
      response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {"role": "system", "content": system_prompt},
          {"role": "user", "content" : user_prompt}
        ],
        temperature=0.7,
        max_tokens=500,
      )

      content = response.choices[0].message.content
      print("[generate_scenario_from_slang] OpenAI 응답:", content)

      # JSON 배열로 변환
      scenario_list = json.loads(content)
      print("[generate_scenario_from_slang] 파싱된 시나리오 리스트:", scenario_list)

      # 최종 결과 리스트 반환
      return scenario_list
  
    except json.JSONDecodeError as e:
      print("[generate_scenario_from_slang] JSON 파싱 오류:", str(e))
      raise ValueError("OpenAI API 응답이 JSON 형식이 아닙니다.")
    except Exception as e:
      print("[generate_scenario_from_slang] 예외 발생:", str(e))
      raise e
    

# "사용자에게서 줄임말을 입력받으면, 그 줄임말의 의미를 상황극처럼 보여주는 이야기 4줄을 만들어줘.\n"
#     "각 문장은 컷툰의 한 장면이 되므로, 구체적인 시각적 요소와 인물의 행동이 묘사되어야 해.\n"
#     "예: '혼코노' ➝ ['고양이 한 마리가 혼자 노래방에 들어선다.', '마이크를 잡고 신나게 노래를 부르기 시작한다.', ...]"

# user_prompt = f"줄임말: {slang}"

# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": system_prompt},
#     {"role": "user", "content" : user_prompt}
#   ],
#   temperature=0.8
# )

# scenario_text = response.choices[0].message.content.strip()
# scenario_lines = [line.strip("- ").strip() for line in scenario_text.split("\n") if line.strip()]

# return scenario_lines[:4] #4줄만 반환