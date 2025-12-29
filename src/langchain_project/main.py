"""Main module for the LangChain project."""

import argparse
import importlib.util
import sys
from pathlib import Path
from dotenv import load_dotenv
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

# Load environment variables from .env file
load_dotenv()
console = Console()


def find_script(model: str, script_name: str, category: str = None) -> Path:
    """
    Find a script in the project structure.

    Args:
        model: The model provider (gemini or openai)
        script_name: The script name to execute (without .py extension)
        category: Optional category folder (e.g., 'fundamentos', 'chains-e-processamento')

    Returns:
        Path to the script file
    """
    # Add .py extension if not present
    if not script_name.endswith('.py'):
        script_name = f"{script_name}.py"

    base_src = Path(__file__).parent.parent

    # If category is specified, look there directly
    if category:
        script_path = base_src / f"_{category}" / f"_{model}" / script_name
        if script_path.exists():
            return script_path

    # Search in all directories that match the pattern _*/_model/
    for category_dir in base_src.glob("_*"):
        if category_dir.is_dir():
            model_dir = category_dir / f"_{model}"
            if model_dir.is_dir():
                script_path = model_dir / script_name
                if script_path.exists():
                    return script_path

    return None


def run_script(model: str, script_name: str, category: str = None) -> None:
    """
    Execute a script from any category directory.

    Args:
        model: The model provider (gemini or openai)
        script_name: The script name to execute (without .py extension)
        category: Optional category folder name
    """
    script_path = find_script(model, script_name, category)

    if not script_path:
        console.print(f"[bold red]❌ Erro:[/bold red] Script '{script_name}' não encontrado para o modelo '{model}'")

        # List available scripts
        base_src = Path(__file__).parent.parent
        console.print(f"\n[bold cyan]📁 Scripts disponíveis para '{model}':[/bold cyan]\n")

        found_any = False
        tree = Tree(f"[bold yellow]{model}[/bold yellow]")

        for category_dir in sorted(base_src.glob("_*")):
            if category_dir.is_dir():
                model_dir = category_dir / f"_{model}"
                if model_dir.is_dir():
                    scripts = list(model_dir.glob("*.py"))
                    if scripts:
                        found_any = True
                        category_name = category_dir.name[1:]  # Remove leading underscore
                        branch = tree.add(f"[cyan]{category_name}[/cyan]")
                        for script in sorted(scripts):
                            branch.add(f"[green]{script.name}[/green]")

        if found_any:
            console.print(tree)
        else:
            console.print(f"  [yellow]Nenhum script encontrado para o modelo '{model}'[/yellow]")

        sys.exit(1)

    # Get category name for display
    category_name = script_path.parent.parent.name[1:]

    console.rule(f"[bold cyan]Executando Script[/bold cyan]")
    console.print(f"[bold green]📄 Script:[/bold green] {script_path.name}")
    console.print(f"[bold yellow]📦 Modelo:[/bold yellow] {model}")
    console.print(f"[bold blue]📂 Categoria:[/bold blue] {category_name}")
    console.rule(style="dim")

    # Load and execute the module
    spec = importlib.util.spec_from_file_location("dynamic_module", script_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules["dynamic_module"] = module
        spec.loader.exec_module(module)
    else:
        console.print(f"[bold red]❌ Erro ao carregar o módulo:[/bold red] {script_path}")
        sys.exit(1)


def main() -> None:
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description="Execute scripts LangChain com diferentes modelos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  uv run langchain gemini hello-world
  uv run langchain openai iniciando-com-chains
  uv run langchain gemini hello-world.py
  uv run langchain openai chat-prompt-template --category fundamentos
        """
    )

    parser.add_argument(
        "model",
        choices=["gemini", "openai"],
        help="Modelo a ser utilizado (gemini ou openai)"
    )

    parser.add_argument(
        "script",
        help="Nome do script a ser executado (com ou sem .py)"
    )

    parser.add_argument(
        "--category",
        "-c",
        help="Categoria específica onde procurar o script (opcional)"
    )

    args = parser.parse_args()

    run_script(args.model, args.script, args.category)


if __name__ == "__main__":
    main()
