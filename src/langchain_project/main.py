"""Main module for the LangChain project."""

import argparse
import importlib.util
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


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
        print(f"❌ Erro: Script '{script_name}' não encontrado para o modelo '{model}'")

        # List available scripts
        base_src = Path(__file__).parent.parent
        print(f"\n📁 Scripts disponíveis para '{model}':\n")

        found_any = False
        for category_dir in sorted(base_src.glob("_*")):
            if category_dir.is_dir():
                model_dir = category_dir / f"_{model}"
                if model_dir.is_dir():
                    scripts = list(model_dir.glob("*.py"))
                    if scripts:
                        found_any = True
                        category_name = category_dir.name[1:]  # Remove leading underscore
                        print(f"  [{category_name}]")
                        for script in sorted(scripts):
                            print(f"    - {script.name}")
                        print()

        if not found_any:
            print(f"  Nenhum script encontrado para o modelo '{model}'")

        sys.exit(1)

    # Get category name for display
    category_name = script_path.parent.parent.name[1:]

    print(f"🚀 Executando: {script_path.name}")
    print(f"📦 Modelo: {model}")
    print(f"📂 Categoria: {category_name}")
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
  poetry run langchain openai iniciando-com-chains
  poetry run langchain gemini hello-world.py
  poetry run langchain openai chat-prompt-template --category fundamentos
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
