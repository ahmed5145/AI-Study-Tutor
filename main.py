from openai import OpenAI

client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a skilled expert programming engineer, skilled in explaining complex programming concepts with creative flair and understandable examples."},
    {"role": "user", "content": "I am a college student."}
  ]
)

print(completion.choices[0].message)