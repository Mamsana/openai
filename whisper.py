import requests

url = "https://whisper.lablab.ai/asr"
payload = {}
files = [ ('audio_file',('audio.mp3',open('audio.mp3','rb'),'audio/mpeg')) ]
response = requests.request("POST", url, data=payload, files=files)
prompt = response.json()["text"]
print(prompt)
