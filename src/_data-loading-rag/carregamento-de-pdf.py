import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich import print

script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(script_dir, "gpt5.pdf")

loader = PyPDFLoader(pdf_path)
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = splitter.split_documents(docs)

print(f"[bold green]Total de chunks gerados:[/bold green] {len(chunks)}")
