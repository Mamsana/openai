import requests
import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.environ["OPENAI_API_KEY"]

url = "https://whisper.lablab.ai/asr"

payload = {}
files = [ ('audio_file',('audio.mp3',open('audio.mp3','rb'),'audio/mpeg')) ]
response = requests.request("POST", url, data=payload, files=files)
prompt = response.json()["text"]
print("The following statement is from your audio:\n{}".format(prompt))

text = prompt
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Please generate a high quality and detailed image prompt for dall-e 2 based on the following: '" + text + "'.",
  temperature=0.7,
  max_tokens=2500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
prompt = response.choices[0].text
print("\nBased on the above statement, you got this prompt:{}".format(prompt))

url = "https://api.openai.com/v1/images/generations"
prompt = prompt
model = "image-alpha-001"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
}
data = {
    "model": model,
    "prompt": prompt,
    "num_images": 1,
    "size": "256x256",
    "response_format": "url"
}
response = requests.post(url, headers=headers, json=data)
response_data = response.json().get("data", [])
image_url = response_data[0].get("url")
print ("\nThe generated image is at: {}".format(image_url))
