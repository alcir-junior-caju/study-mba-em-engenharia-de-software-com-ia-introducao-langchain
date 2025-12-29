from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
message = model.invoke("Hello World")

print("[bold green]Resposta:[/bold green]")
print(message.content)
