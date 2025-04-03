import requests

def request_colab_images(prompt : str):
  response = requests.post(
    "http://<NGROK_URL>/generate",
    json={"prompt" : prompt}
  )
  return response.json().get("images", [])