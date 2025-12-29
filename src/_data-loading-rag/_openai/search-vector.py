import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from rich import print
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()
for k in ("OPENAI_API_KEY", "PGVECTOR_URL","PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")


query = "Tell me more about the gpt-5 thinking evaluation and performance results comparing to gpt-4"

embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

results = store.similarity_search_with_score(query, k=3)

for i, (doc, score) in enumerate(results, start=1):
    console.rule(f"[bold cyan]Resultado {i}[/bold cyan]")
    print(f"[yellow]Score:[/yellow] {score:.2f}")

    print("\n[bold green]Texto:[/bold green]")
    print(doc.page_content.strip())

    print("\n[bold blue]Metadados:[/bold blue]")
    for k, v in doc.metadata.items():
        print(f"  [cyan]{k}:[/cyan] {v}")
    print()
