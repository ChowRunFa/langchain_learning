'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003",max_tokens=200)
text = llm("请给我写一句情人节红玫瑰的中文宣传语")
print(text)