from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv
from rich import print

load_dotenv()

@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression and return the result as a string."""
    try:
        result = eval(expression)  # cuidado: apenas para exemplo didático
    except Exception as e:
        return f"Error: {e}"
    return str(result)

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Return the capital of a given country if it exists in the mock data."""
    data = {
        "Brazil": "Brasília",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United States": "Washington, D.C."

    }
    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"The capital of {country} is {capital}."
    return "I don't know the capital of that country."

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
tools = [web_search_mock]

prompt = hub.pull("hwchase17/react")
agent_chain = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent_chain,
    tools=tools,
    verbose=True,
    # max_iterations=5
)

print("[bold cyan]Query: Capital of Iran[/bold cyan]")
result = agent_executor.invoke({"input": "What is the capital of Iran?"})
print("[bold green]Resposta:[/bold green]")
print(result)
# print(agent_executor.invoke({"input": "How much is 10 + 10?"}))
