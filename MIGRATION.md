# Migração de Poetry para uv

## ✨ O que mudou?

Este projeto foi migrado do **Poetry** para o **uv**, uma ferramenta de gerenciamento de pacotes Python ultra-rápida desenvolvida pela Astral (mesma empresa por trás do Ruff).

## 🚀 Por que uv?

- **10-100x mais rápido** que pip e Poetry
- **Instalação simplificada** de dependências
- **Compatível** com o formato pyproject.toml padrão
- **Menos configuração** necessária
- **Gerenciamento automático** de ambientes virtuais

## 📋 Mudanças nos Comandos

### Antes (Poetry)
```bash
poetry install                      # Instalar dependências
poetry add pacote                   # Adicionar pacote
poetry add --group dev pacote       # Adicionar pacote dev
poetry run python script.py         # Executar script
poetry shell                        # Ativar ambiente virtual
poetry update                       # Atualizar dependências
```

### Agora (uv)
```bash
uv sync                             # Instalar/sincronizar dependências
uv add pacote                       # Adicionar pacote
uv add --dev pacote                 # Adicionar pacote dev
uv run python script.py             # Executar script
source .venv/bin/activate           # Ativar ambiente virtual
uv lock --upgrade                   # Atualizar dependências
```

## 🔄 Arquivos Alterados

### Adicionados
- `uv.lock` - Arquivo de lock do uv (equivalente ao poetry.lock)

### Modificados
- `pyproject.toml` - Convertido para formato padrão PEP 621
- `Instructions.md` - Atualizado com comandos do uv
- `src/langchain_project/main.py` - Exemplos atualizados

### Removidos
- `poetry.lock` - Arquivo de lock do Poetry
- `.venv/` (do Poetry) - Recriado pelo uv

## 🛠️ Como Migrar Seu Ambiente Local

Se você já tinha o projeto instalado com Poetry, siga estes passos:

1. **Instale o uv**:
   ```bash
   # macOS e Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Ou via pip
   pip install uv
   ```

2. **Remova o ambiente virtual antigo**:
   ```bash
   rm -rf .venv
   ```

3. **Sincronize as dependências**:
   ```bash
   uv sync
   ```

4. **Teste a instalação**:
   ```bash
   uv run python -c "import langchain; print('Sucesso!')"
   ```

## 📚 Executando os Scripts

Os comandos para executar os scripts mudaram. Consulte o [Instructions.md](Instructions.md) para exemplos completos.

Exemplo rápido:
```bash
# Antes
poetry run python src/_fundamentos/_openai/hello-world.py

# Agora
uv run python src/_fundamentos/_openai/hello-world.py
```

## 🐛 Problemas Conhecidos

Se você encontrar algum problema:

1. Certifique-se de que o uv está instalado: `uv --version`
2. Verifique se está no diretório correto do projeto
3. Tente remover `.venv` e executar `uv sync` novamente
4. Consulte a documentação oficial: https://docs.astral.sh/uv/

## 📖 Mais Informações

- [Documentação oficial do uv](https://docs.astral.sh/uv/)
- [Comparação de performance](https://github.com/astral-sh/uv#benchmarks)
- [Guia de migração do Poetry](https://docs.astral.sh/uv/guides/projects/#migrating-from-poetry)
