import requests
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

url = "https://whisper.lablab.ai/asr"

payload = {}
files = [ ('audio_file',('audio.mp3',open('audio.mp3','rb'),'audio/mpeg')) ]
response = requests.request("POST", url, data=payload, files=files)
text = response.json()["text"]
print("The following message is from your audio:{}".format(text))

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Please generate a high quality and detailed image prompt for dall-e 2 based on the following: '" + text + "'.",
  temperature=0.7,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
prompt = response.choices[0].text
print("\nBased on the above statement, you got this prompt:{}".format(prompt))

response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']
print ("\nThe generated image is at: {}".format(image_url))
