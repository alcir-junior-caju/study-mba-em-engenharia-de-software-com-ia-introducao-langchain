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
│   │   ├── _openai/
│   │   │   ├── hello-world.py
│   │   │   └── chat-prompt-template.py
│   │   └── prompt-template.py
│   ├── _chains-e-processamento/
│   │   ├── _gemini/
│   │   │   ├── iniciando-com-chains.py
│   │   │   ├── chains-decorator.py
│   │   │   ├── pipeline-de-processamento.py
│   │   │   ├── pipeline-de-sumarizacao.py
│   │   │   ├── sumarizacao.py
│   │   │   └── sumarizacao-com-map-reduce.py
│   │   ├── _openai/
│   │   │   ├── iniciando-com-chains.py
│   │   │   ├── chains-decorator.py
│   │   │   ├── pipeline-de-processamento.py
│   │   │   ├── pipeline-de-sumarizacao.py
│   │   │   ├── sumarizacao.py
│   │   │   └── sumarizacao-com-map-reduce.py
│   │   └── runnable-lambda.py
│   ├── _agentes-e-tools/
│   │   ├── _gemini/
│   │   │   ├── agente-react-e-tools.py
│   │   │   └── agente-react-usando-prompt-hub.py
│   │   └── _openai/
│   │       ├── agente-react-e-tools.py
│   │       └── agente-react-usando-prompt-hub.py
│   ├── _data-loading-rag/
│   │   ├── _gemini/
│   │   │   ├── ingestion-pgvector.py
│   │   │   └── search-vector.py
│   │   ├── _openai/
│   │   │   ├── ingestion-pgvector.py
│   │   │   └── search-vector.py
│   │   ├── carregamento-de-pdf.py
│   │   ├── carregamento-usando-WebBaseLoader.py
│   │   └── gpt5.pdf
│   ├── _gerenciamento-memoria/
│   │   ├── _gemini/
│   │   │   ├── armazenamento-de-historico.py
│   │   │   └── historico-baseado-em-sliding-window.py
│   │   └── _openai/
│   │       ├── armazenamento-de-historico.py
│   │       └── historico-baseado-em-sliding-window.py
│   └── langchain_project/
│       └── main.py
├── tests/
│   └── __init__.py
├── docker-compose.yaml
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
- **langchain-community**: Ferramentas e integrações da comunidade
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **beautifulsoup4**: Web scraping e parsing HTML
- **pypdf**: Manipulação de arquivos PDF
- **pgvector**: Extensão PostgreSQL para vetores (RAG)
- **psycopg2-binary**: Driver PostgreSQL para Python

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

### 4. Configuração do PostgreSQL (para exemplos de RAG)

O projeto inclui um PostgreSQL com pgvector para os exemplos de RAG. Para iniciar o banco de dados:

```bash
# Iniciar o PostgreSQL com pgvector
docker-compose up -d

# Verificar se está rodando
docker-compose ps

# Parar o PostgreSQL
docker-compose down

# Parar e remover volumes (apaga dados)
docker-compose down -v
```

O banco estará disponível em:
- **Host**: localhost
- **Porta**: 5432
- **Usuário**: postgres
- **Senha**: postgres
- **Database**: rag

## 💻 Uso

### Categorias de Exemplos

#### 🔰 Fundamentos
Conceitos básicos do LangChain:
- **hello-world.py**: Primeira interação com LLMs
- **chat-prompt-template.py**: Templates de prompts estruturados
- **prompt-template.py**: Templates básicos de prompts

#### 🔗 Chains e Processamento
Pipelines e encadeamento de operações:
- **iniciando-com-chains.py**: Introdução a chains
- **chains-decorator.py**: Uso de decorators para criar chains
- **pipeline-de-processamento.py**: Pipelines complexos
- **pipeline-de-sumarizacao.py**: Pipeline específico de sumarização
- **sumarizacao.py**: Sumarização de textos
- **sumarizacao-com-map-reduce.py**: Sumarização usando estratégia MapReduce
- **runnable-lambda.py**: Uso de Runnable Lambda

#### 🤖 Agentes e Tools
Agentes inteligentes com ferramentas:
- **agente-react-e-tools.py**: Agentes ReAct com ferramentas personalizadas
- **agente-react-usando-prompt-hub.py**: Agentes usando prompts do LangChain Hub

#### 📚 Data Loading e RAG
Carregamento de dados e Retrieval-Augmented Generation:
- **carregamento-de-pdf.py**: Carregamento e processamento de PDFs
- **carregamento-usando-WebBaseLoader.py**: Carregamento de conteúdo web
- **ingestion-pgvector.py**: Ingestão de dados em PostgreSQL com pgvector
- **search-vector.py**: Busca semântica usando vetores

#### 💾 Gerenciamento de Memória
Persistência e gerenciamento de histórico de conversações:
- **armazenamento-de-historico.py**: Armazenamento de histórico de chat
- **historico-baseado-em-sliding-window.py**: Gerenciamento com janela deslizante

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
poetry run python src/_chains-e-processamento/_openai/chains-decorator.py
poetry run python src/_chains-e-processamento/_openai/pipeline-de-processamento.py
poetry run python src/_chains-e-processamento/_openai/pipeline-de-sumarizacao.py
poetry run python src/_chains-e-processamento/_openai/sumarizacao.py
poetry run python src/_chains-e-processamento/_openai/sumarizacao-com-map-reduce.py

# Chains com Google Gemini
poetry run python src/_chains-e-processamento/_gemini/iniciando-com-chains.py
poetry run python src/_chains-e-processamento/_gemini/chains-decorator.py
poetry run python src/_chains-e-processamento/_gemini/pipeline-de-processamento.py
poetry run python src/_chains-e-processamento/_gemini/pipeline-de-sumarizacao.py
poetry run python src/_chains-e-processamento/_gemini/sumarizacao.py
poetry run python src/_chains-e-processamento/_gemini/sumarizacao-com-map-reduce.py

# Runnable Lambda (independente de modelo)
poetry run python src/_chains-e-processamento/runnable-lambda.py
```

#### Agentes e Tools

```bash
# Agentes com OpenAI
poetry run python src/_agentes-e-tools/_openai/agente-react-e-tools.py
poetry run python src/_agentes-e-tools/_openai/agente-react-usando-prompt-hub.py

# Agentes com Google Gemini
poetry run python src/_agentes-e-tools/_gemini/agente-react-e-tools.py
poetry run python src/_agentes-e-tools/_gemini/agente-react-usando-prompt-hub.py
```

#### Data Loading e RAG

```bash
# Carregamento de dados (independente de modelo)
poetry run python src/_data-loading-rag/carregamento-de-pdf.py
poetry run python src/_data-loading-rag/carregamento-usando-WebBaseLoader.py

# RAG com OpenAI
poetry run python src/_data-loading-rag/_openai/ingestion-pgvector.py
poetry run python src/_data-loading-rag/_openai/search-vector.py

# RAG com Google Gemini
poetry run python src/_data-loading-rag/_gemini/ingestion-pgvector.py
poetry run python src/_data-loading-rag/_gemini/search-vector.py
```

#### Gerenciamento de Memória

```bash
# Memória com OpenAI
poetry run python src/_gerenciamento-memoria/_openai/armazenamento-de-historico.py
poetry run python src/_gerenciamento-memoria/_openai/historico-baseado-em-sliding-window.py

# Memória com Google Gemini
poetry run python src/_gerenciamento-memoria/_gemini/armazenamento-de-historico.py
poetry run python src/_gerenciamento-memoria/_gemini/historico-baseado-em-sliding-window.py
```

### Atalho com Poetry Shell

Para executar vários scripts sem repetir `poetry run`:

```bash
# Ativar o shell do ambiente virtual
poetry shell

# Agora execute diretamente (exemplos)
python src/_fundamentos/_openai/hello-world.py
python src/_chains-e-processamento/_gemini/iniciando-com-chains.py
python src/_agentes-e-tools/_openai/agente-react-e-tools.py
python src/_data-loading-rag/_gemini/search-vector.py
python src/_gerenciamento-memoria/_openai/armazenamento-de-historico.py
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
├── _fundamentos/              # Conceitos básicos do LangChain
│   ├── _gemini/              # Exemplos usando Google Gemini
│   ├── _openai/              # Exemplos usando OpenAI
│   └── prompt-template.py    # Template básico de prompts
├── _chains-e-processamento/   # Chains e pipelines
│   ├── _gemini/              # Implementações com Gemini
│   ├── _openai/              # Implementações com OpenAI
│   └── runnable-lambda.py    # Exemplo de Runnable Lambda
├── _agentes-e-tools/          # Agentes e ferramentas
│   ├── _gemini/              # Agentes ReAct com Gemini
│   └── _openai/              # Agentes ReAct com OpenAI
├── _data-loading-rag/         # Carregamento de dados e RAG
│   ├── _gemini/              # RAG com Gemini e pgvector
│   ├── _openai/              # RAG com OpenAI e pgvector
│   ├── carregamento-de-pdf.py
│   ├── carregamento-usando-WebBaseLoader.py
│   └── gpt5.pdf              # Arquivo de exemplo
└── _gerenciamento-memoria/    # Gerenciamento de histórico
    ├── _gemini/              # Memória com Gemini
    └── _openai/              # Memória com OpenAI
```

### Adicionar Novos Scripts

Para adicionar um novo script:

1. Escolha a categoria apropriada (ou crie uma nova pasta `_categoria/`)
2. Crie subpastas `_gemini/` e `_openai/` se necessário
3. Adicione seu script Python:

```python
# src/_fundamentos/_openai/meu_script.py
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Seu código aqui
model = ChatOpenAI(model="gpt-4")
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
