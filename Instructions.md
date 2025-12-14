# 📖 Instruções - LangChain Project

## 🚀 Configuração do Ambiente

### Estrutura do Projeto

```
langchain/
├── src/
│   └── langchain_project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── __init__.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── Instructions.md
```

### Dependências Principais

- **langchain**: Framework para desenvolvimento de aplicações com LLMs
- **langchain-openai**: Integração com modelos OpenAI
- **langchain-google-genai**: Integração com Google GenAI
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **beautifulsoup4**: Web scraping e parsing HTML
- **pypdf**: Manipulação de arquivos PDF

### Dependências de Desenvolvimento

- **pytest**: Framework de testes
- **black**: Formatador de código
- **ruff**: Linter rápido
- **mypy**: Verificador de tipos estáticos

## 📋 Configuração

### 1. Pré-requisitos

- Python 3.9 ou superior
- Poetry 2.x

### 2. Instalação

O Poetry já criou e ativou o ambiente virtual automaticamente durante a instalação:

```bash
poetry install
```

### 3. Configuração de Variáveis de Ambiente

Copie o arquivo de exemplo e configure suas chaves de API:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione suas chaves de API:

```env
OPENAI_API_KEY=sua_chave_openai_aqui
GOOGLE_API_KEY=sua_chave_google_aqui
```

## 💻 Uso

### Executar o Projeto

```bash
# Usando poetry run
poetry run python src/langchain_project/main.py

# Ou usando o script configurado
poetry run langchain-project

# Ou ativando o shell do poetry
poetry shell
python src/langchain_project/main.py
```

### Executar Testes

```bash
poetry run pytest
```

### Formatação e Linting

```bash
# Formatar código com Black
poetry run black src/ tests/

# Verificar código com Ruff
poetry run ruff check src/ tests/

# Verificar tipos com MyPy
poetry run mypy src/
```

## 🛠️ Comandos Úteis do Poetry

```bash
# Ativar o shell do ambiente virtual
poetry shell

# Adicionar uma nova dependência
poetry add nome-do-pacote

# Adicionar uma dependência de desenvolvimento
poetry add --group dev nome-do-pacote

# Atualizar dependências
poetry update

# Mostrar dependências instaladas
poetry show

# Informações sobre o ambiente virtual
poetry env info
```

## 📝 Desenvolvimento

### Adicionar Novos Módulos

Crie novos arquivos Python dentro de `src/langchain_project/`:

```python
# src/langchain_project/meu_modulo.py
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def minha_funcao():
    # Seu código aqui
    pass
```

### Adicionar Testes

Crie arquivos de teste em `tests/`:

```python
# tests/test_meu_modulo.py
from langchain_project.meu_modulo import minha_funcao

def test_minha_funcao():
    resultado = minha_funcao()
    assert resultado is not None
```

## ✅ Melhores Práticas Implementadas

- ✅ **Estrutura de Pacote**: Código organizado em `src/` para melhor isolamento
- ✅ **Ambiente Virtual**: Gerenciado automaticamente pelo Poetry
- ✅ **Dependências**: Versionamento preciso com Poetry
- ✅ **Variáveis de Ambiente**: Usando python-dotenv para configurações sensíveis
- ✅ **Formatação**: Black configurado para código consistente
- ✅ **Linting**: Ruff para código limpo e sem erros
- ✅ **Type Checking**: MyPy para verificação de tipos
- ✅ **Testes**: Estrutura pronta com pytest
- ✅ **Git**: .gitignore configurado para Python
