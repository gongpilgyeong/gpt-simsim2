import os

import openai
import config
from dotenv import load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="""
    Fix grammar errors:
    - I is a boy
    - You is a girl""".strip(),
)

print(response)

print(response.choices[0].text.strip())


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 지식이 풍부한 도우미입니다."},
        {"role": "user", "content": "세계에서 가장 큰 도시는 어디인가요?"},
    ],
)

print(response)
print(response["choices"][0]["messages"]["content"])
