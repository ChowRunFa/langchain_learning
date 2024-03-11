'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# 设置OpenAI和SERPAPI的API密钥
import dotenv
dotenv.load_dotenv()

# 加载所需的库
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(
        model_name="chatglm",
        openai_api_base="http://localhost:8000/v1",
        openai_api_key="EMPTY",
        streaming=False,
    )

# 设置工具
# llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 初始化Agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 跑起来
# agent.run("目前市场上玫瑰花的平均价格是多少？如果我在此基础上加价15%卖出，应该如何定价？")
agent.run("目前美国总统是谁？多少岁了？")