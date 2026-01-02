from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(
    model=llm,
    tools=tools
)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="Search for 5 job postings for an AI engineer using LangChain in the Montreal area on LinkedIn and Indeed and list theit details.")})
    print(result)


if __name__ == "__main__":
    main()
