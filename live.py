import requests # for sending HTTP requests
import os # for accessing environment variables
import openai # for accessing OpenAI's API

# Setting the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# URL of the ASR service (Automatic Speech Recognition service)
url = "https://whisper.lablab.ai/asr"

# Creating an empty payload dictionary
payload = {}

# Creating a list of tuples containing the file to be uploaded
files = [ ('audio_file',('audio.mp3',open('audio.mp3','rb'),'audio/mpeg')) ]

# Sending a HTTP POST request to the ASR service with the file to be transcribed
response = requests.request("POST", url, data=payload, files=files)

# Extracting and printing the transcribed text from the response JSON
text = response.json()["text"]
print("The following message is from your audio:{}".format(text))


# Creating a prompt for generating an image based on the transcribed text using OpenAI's GPT-3
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Please generate a high quality and detailed image prompt for dall-e 2 based on the following: '" + text + "'.",
  temperature=0.7,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Extracting and printing the prompt for generating the image from the OpenAI API response
prompt = response.choices[0].text
print("\nBased on the above statement, you got this prompt:{}".format(prompt))


# Generating an image based on the prompt using OpenAI's DALL-E API
response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="512x512"
)

# Extracting and printing the URL of the generated image from the OpenAI API response
image_url = response['data'][0]['url']
print ("\nThe generated image is at: {}".format(image_url))

# Send a request to the url and receive the response
response = requests.get(image_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content of the response (the image data)
    image_data = response.content
    
    # Save the image data to a file
    with open("image.jpg", "wb") as f:
        f.write(image_data)
        print("Image saved successfully!")
else:
    print("Failed to download image.")
