from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import SystemMessage

# model = ChatOpenAI()

# gemini-3-pro-image-preview / gemini-3-pro-preview / gemini-3-flash-preview
# 需要爬梯
model = ChatGoogleGenerativeAI(model='gemini-3-pro-preview', vertexai=False)

sysprompt = SystemMessage(content="you are a helpful assist agent")

agent = create_agent(model, system_prompt=sysprompt, name="weatherman_assistant")


result = agent.invoke({"messages": [{"role": "user", "content": "what is the weather in BeiJing"}]})

print(result)
