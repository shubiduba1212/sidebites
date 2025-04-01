import json
import requests
import os

WORKFLOW_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "generate_image_workflow.json")

def generate_comic_image(prompt_text: str):
    with open(WORKFLOW_PATH, "r", encoding="utf-8") as f:
        workflow = json.load(f)

    nodes = workflow["nodes"]

    # ✅ class_type 자동 추가 + 디버깅
    missing_class_type = [node for node in nodes if "class_type" not in node]
    print(f"🧩 class_type 누락된 노드 수: {len(missing_class_type)}")
    for node in nodes:
        if "type" in node and "class_type" not in node:
            print(f"⚠️ 누락된 노드 → id: {node.get('id')}, type: {node.get('type')}")
            node["class_type"] = node["type"]

    # ✅ 프롬프트 텍스트 적용
    for node in nodes:
        if node.get("type") == "CLIPTextEncode":
            node["widgets_values"][0] = prompt_text

    # ✅ 올바른 전체 구조로 전송
    payload = {
        "prompt": {
            "nodes": workflow["nodes"],
            "links": workflow["links"],
            "extra": workflow.get("extra", {}),
            "version": workflow.get("version", 0.4)
        }
    }

    print("🔼 ComfyUI에 요청 전송 중...")
    response = requests.post("http://127.0.0.1:8188/prompt", json=payload)

    print("✅ 응답 수신 완료:", response.status_code)
    print("📦 응답 내용:", response.text)

    result = response.json()

    # ✅ 이미지 URL 파싱
    try:
        outputs = result.get("outputs", {})
        for node_output in outputs.values():
            images = node_output.get("images", [])
            if images:
                filename = images[0]["filename"]
                return f"http://localhost:8188/view?filename={filename}"
    except Exception as e:
        print("ComfyUI 응답 파싱 실패:", e)

    return None




# def build_comic_prompt(slang: str, meaning: str) -> str:
#     return f"""
# 슬랭 '{slang}({meaning})'를 주제로 한 4컷 만화를 기획해줘.
# 각 컷은 다음과 같은 내용을 담고 있어:

# 1. 이 슬랭의 상황을 암시하는 시작 장면
# 2. 상황이 전개되는 중간 장면
# 3. 감정이 폭발하거나 반전이 있는 클라이맥스
# 4. 슬랭을 이해할 수 있는 마무리 또는 교훈적인 장면

# 스타일은 귀엽고 감성적인 만화 스타일이고, 현대적인 도시 배경이면 좋아.
# 각 컷은 간결한 한 문장으로 표현해줘.
# """
