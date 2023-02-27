import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

text = input("Enter your text for image generation:\n")
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
print("This is your prompt for dall-e2: {}".format(prompt))
