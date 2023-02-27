import requests
import json
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

url = "https://api.openai.com/v1/images/generations"
prompt = input("Enter your prompt for DALL-E2\n")
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
print ("The generated image is at {}".format(image_url))
