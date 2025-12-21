# 📖 Instruções - LangChain Project

## 🚀 Configuração do Ambiente

### Estrutura do Projeto

```
langchain/
├── src/
│   ├── _fundamentos/
│   │   ├── _gemini/
│   │   │   ├── hello-world.py
│   │   │   └── chat-prompt-template.py
│   │   └── _openai/
│   │       ├── hello-world.py
│   │       └── chat-prompt-template.py
│   └── _chains-e-processamento/
│       ├── _gemini/
│       │   └── iniciando-com-chains.py
│       └── _openai/
│           └── iniciando-com-chains.py
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

Instale as dependências do projeto:

```bash
poetry install
```

O Poetry criará e ativará o ambiente virtual automaticamente.

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

### Executar Scripts

Os scripts estão organizados por categoria e modelo. Execute-os diretamente:

#### Fundamentos

```bash
# Hello World com OpenAI
poetry run python src/_fundamentos/_openai/hello-world.py

# Hello World com Google Gemini
poetry run python src/_fundamentos/_gemini/hello-world.py

# Chat Prompt Template com OpenAI
poetry run python src/_fundamentos/_openai/chat-prompt-template.py

# Chat Prompt Template com Google Gemini
poetry run python src/_fundamentos/_gemini/chat-prompt-template.py

# Prompt Template básico
poetry run python src/_fundamentos/prompt-template.py
```

#### Chains e Processamento

```bash
# Chains com OpenAI
poetry run python src/_chains-e-processamento/_openai/iniciando-com-chains.py

# Chains com Google Gemini
poetry run python src/_chains-e-processamento/_gemini/iniciando-com-chains.py
```

### Atalho com Poetry Shell

Para executar vários scripts sem repetir `poetry run`:

```bash
# Ativar o shell do ambiente virtual
poetry shell

# Agora execute diretamente
python src/_fundamentos/_openai/hello-world.py
python src/_chains-e-processamento/_gemini/iniciando-com-chains.py
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

### Estrutura de Pastas

O projeto segue uma estrutura organizada por tópicos:

```
src/
├── _fundamentos/           # Conceitos básicos do LangChain
│   ├── _gemini/           # Exemplos usando Google Gemini
│   └── _openai/           # Exemplos usando OpenAI
└── _chains-e-processamento/  # Chains e pipelines
    ├── _gemini/
    └── _openai/
```

### Adicionar Novos Scripts

Para adicionar um novo script:

1. Escolha a categoria apropriada (ou crie uma nova pasta `_categoria/`)
2. Crie subpastas `_gemini/` e `_openai/` se necessário
3. Adicione seu script Python:
fundamentos.py
def test_exemplo():
    # Seus testes aqui
    assert Tru
load_dotenv()

# Seu código aqui
model = ChatOpenAI(model="gpt-5-mini")
result = model.invoke("Hello!")
print(result.content)
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
