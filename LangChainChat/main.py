import os
from secret import API_KEY
os.environ["OPENAI_API_KEY"] = API_KEY
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.schema import HumanMessage

llm = OpenAI()
chat_model = ChatOpenAI()

text = "Where is Brazil?"
messages = [HumanMessage(content=text)]

llm.invoke(text)
print(chat_model.invoke(messages))