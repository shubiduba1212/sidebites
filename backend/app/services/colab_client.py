import requests
from dotenv import load_dotenv
import os

load_dotenv()
COLAB_URL = os.getenv("COLAB_FLASK_URL")
ngrok_url = COLAB_URL + "/generate"

def request_colab_images(prompt : str):
  response = requests.post(
    # "http://<NGROK_URL>/generate",
    ngrok_url,
    json={"prompt" : prompt}
  )
  return response.json().get("images", [])