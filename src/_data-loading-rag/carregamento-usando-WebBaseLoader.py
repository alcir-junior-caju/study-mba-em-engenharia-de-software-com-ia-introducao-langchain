from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich import print
from rich.console import Console

console = Console()

loader = WebBaseLoader("https://www.langchain.com/")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = splitter.split_documents(docs)

for i, chunk in enumerate(chunks, 1):
    console.rule(f"[bold cyan]Chunk {i}[/bold cyan]")
    print(chunk)
