# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv

client = OpenAI(api_key="sk-41797a635e3c4cd0b63d1013f35ad665", base_url="https://api.deepseek.com")
input_text = input ("enter your text")
response = client.chat.completions.create(
    model="deepseek-chat",
    store=True,
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)