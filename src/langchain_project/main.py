"""Main module for the LangChain project."""

import argparse
import importlib.util
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def run_script(model: str, script_name: str) -> None:
    """
    Execute a script from the fundamentos directory.

    Args:
        model: The model provider (gemini or openai)
        script_name: The script name to execute (without .py extension)
    """
    # Get the base path
    base_path = Path(__file__).parent.parent / "_fundamentos" / f"_{model}"

    # Add .py extension if not present
    if not script_name.endswith('.py'):
        script_name = f"{script_name}.py"

    # Build the script path
    script_path = base_path / script_name

    if not script_path.exists():
        print(f"❌ Erro: Script não encontrado: {script_path}")
        print(f"\nProcurando em: {base_path}")

        # List available scripts
        if base_path.exists():
            available = list(base_path.glob("*.py"))
            if available:
                print("\n📁 Scripts disponíveis:")
                for script in available:
                    print(f"  - {script.name}")
        sys.exit(1)

    print(f"🚀 Executando: {script_path}")
    print(f"📦 Modelo: {model}")
    print("-" * 50)

    # Load and execute the module
    spec = importlib.util.spec_from_file_location("dynamic_module", script_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules["dynamic_module"] = module
        spec.loader.exec_module(module)
    else:
        print(f"❌ Erro ao carregar o módulo: {script_path}")
        sys.exit(1)


def main() -> None:
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description="Execute scripts LangChain com diferentes modelos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  poetry run langchain gemini hello-world
  poetry run langchain openai hello-world
  poetry run langchain gemini hello-world.py
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

    args = parser.parse_args()

    run_script(args.model, args.script)


if __name__ == "__main__":
    main()
