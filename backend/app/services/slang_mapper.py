import json
import os

def load_slang_data():
    file_path = os.path.join(os.path.dirname(__file__), '../data/slang_data.json')
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)

def find_slang(query: str):
    data = load_slang_data()
    for item in data:
        if item["kr_slang"] == query:
            return item
    return {"error": "해당 슬랭을 찾을 수 없습니다."}
