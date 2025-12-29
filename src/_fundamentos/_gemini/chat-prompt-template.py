from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from rich import print
from rich.console import Console

load_dotenv()
console = Console()

system = ("system", "you are an assistant that answers questions in a {style} style")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")

print("[bold cyan]Mensagens:[/bold cyan]")
for msg in messages:
    console.print(f"[yellow]{msg.type}:[/yellow] {msg.content}")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
result = model.invoke(messages)
print("\n[bold green]Resposta:[/bold green]")
print(result.content)
