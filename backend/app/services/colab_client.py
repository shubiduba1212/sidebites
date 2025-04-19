import requests
from dotenv import load_dotenv
import os

load_dotenv()
COLAB_URL = os.getenv("COLAB_FLASK_URL")
ngrok_url = COLAB_URL + "/generate"

def request_colab_images(prompts : list[str]):
  response = requests.post(
    ngrok_url,
    json={"prompts" : prompts}
  )
  return response.json().get("images", [])