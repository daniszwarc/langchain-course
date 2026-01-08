from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4o")

agent = create_agent(
    model=llm,
    tools=tools,
    response_format=ToolStrategy(AgentResponse)
)


def main():
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Search for 3 jobs postings for Agentic AI, GenAI with Langchain in the Montreal area on LinkedIn and list their details"
                }
            ]
        }
    )
    structured = result.get("structured_response", None)
    print(structured if structured is not None else result)


if __name__ == "__main__":
    main()
