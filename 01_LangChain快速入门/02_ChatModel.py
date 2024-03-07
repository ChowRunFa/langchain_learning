import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
from load_glm import llm
model = llm

response = model("请写一篇滕王阁序")

print(response)


