from langchain.prompts import PromptTemplate
from rich import print

template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name!"
)

text = template.format(name="Caju")
print("[bold cyan]Template gerado:[/bold cyan]")
print(text)
