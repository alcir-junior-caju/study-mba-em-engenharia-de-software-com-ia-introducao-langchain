# MBA em Engenharia de Software com IA - Introdução ao LangChain (FullCycle)

<div>
    <img alt="Criado por Alcir Junior [Caju]" src="https://img.shields.io/badge/criado%20por-Alcir Junior [Caju]-%23f08700">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-%23f08700">
</div>

---

## Descrição

Aprenda a usar LangChain para construir pipelines com LLMs, chains, tools e agentes ReAct. Configure o ambiente, chame modelos e desenvolva aplicações com IA generativa de forma prática e estruturada.

---

## Repositório Pai
https://github.com/alcir-junior-caju/study-mba-em-engenharia-de-software-com-ia

---

## Instruções de Configuração e Uso

Para instruções detalhadas sobre configuração do ambiente, instalação, uso e desenvolvimento, consulte o arquivo [Instructions.md](Instructions.md).

---

## Visualizar o projeto na IDE:

Para quem quiser visualizar o projeto na IDE clique no teclado a tecla `ponto`, esse recurso do GitHub é bem bacana

---

# História e Ecossistema LangChain

## Timeline: Do Nascimento ao Unicórnio

* **Outubro de 2022 (Criação):** A LangChain começou a nascer com o **Harrison Chase**, em um contexto de pessoas trabalhando com LLMs, OpenAI, ChatGPT e *prompts*.
* **Abril de 2023 (Startup):** Foi tudo muito rápido. Apenas seis meses após o lançamento inicial, formalizou-se a startup *LangChain*.
    * **Investimento Série A:** A empresa recebeu aportes que somaram aproximadamente **35 milhões de dólares**.
* **Fevereiro de 2024:** Lançamento do **LangSmith**.
* **2025 (Série B):** Foi feito um investimento de série B no valor de **100 milhões de dólares**.
* **Maio de 2025:** Lançamento do **LangGraph Platform**.
* **Valuation Atual:** O valor estimado da empresa hoje é de **1.1 bilhão de dólares**.

## Confiabilidade e Estrutura
O grande ponto de tudo isso é mostrar que a LangChain oferece vários serviços, alguns pagos e outros *open source*.

Se você tem alguma dúvida se vale a pena investir tempo em LangChain para desenvolver aplicações, os números mostram que há muita estrutura por trás do projeto, apesar das bibliotecas serem de código aberto.
É algo realmente confiável, com uma comunidade forte por trás.

> **Exemplo Prático de Cautela:**
> Isso não significa que você deve sair utilizando a ferramenta sem pensar. Confiança não elimina a necessidade de atenção. **Não é porque você está usando um cinto de segurança de última geração que você vai dirigir de olhos fechados.** (Substituição lógica para "sair utilizando sem pensar").

## O Ecossistema de Serviços LangChain
A empresa oferece um conjunto de ferramentas para diferentes necessidades:

### 1. LangGraph & LangGraph Platform
Existe um projeto focado na criação e orquestração de agentes de uma forma bem determinista.
* **LangGraph:** Parte do ecossistema *open source*.
* **LangGraph Platform:** Infraestrutura lançada pela empresa para agentes de IA de longa duração e gerenciamento de *workflows* completos.
* **LangGraph Studio:** Interface visual para o gerenciamento de projetos LangGraph (pode ser plugado à plataforma).

### 2. LangServe - Hosted
* Plataforma para *deploy* de aplicações LangChain.
* Oferece infraestrutura gerenciada e escalabilidade automática.

### 3. LangChain Hub
* Funciona como um catálogo para publicar e versionar *prompts* e cadeias.
* Está integrado a partes do LangSmith (com *playground*).

### 4. LangSmith
* Lançado em fevereiro de 2024.
* É uma plataforma focada intensamente em **observabilidade**, testes e monitoramento.
* Possui correlações com o LangGraph Studio e Platform, permitindo integração entre eles.

# LangChain: Principais Recursos e Ecossistema

## Introdução aos Objetivos
Bom, pessoal, agora que entendemos o ecossistema, vamos focar no que realmente importa: o que a ferramenta faz e o que não faz. A ideia central do LangChain é **simplificar a integração com LLMs (Large Language Models) e serviços auxiliares**.

No dia a dia de quem trabalha com IA, a necessidade primordial é ter fontes de dados.
* **Carregamento de Dados:** Muitas vezes preciso carregar dados externos para usar como contexto.
* **Memória:** Preciso armazenar o histórico para que a IA lembre do que foi dito anteriormente.

> **Exemplo Prático de Contexto:**
> Em vez de apenas carregar dados genéricos, imagine que você precisa **importar um manual técnico de uma geladeira** para que a IA possa responder perguntas específicas de suporte ao cliente baseadas nesse manual.

## Gerenciamento de Documentos e Abstrações
Embora o Python tenha bibliotecas nativas úteis (como PyPDF), o LangChain cria **abstrações** poderosas sobre elas.
* **Splitting (Divisão):** Eles desenvolveram métodos para "splitar" (dividir) documentos. Você pega um arquivo grande e o transforma em pedaços menores (*chunks*) para carregar, guardar e utilizar posteriormente.

> **Analogia de Divisão:**
> Pense nisso como **fatiar um pão de forma inteiro em sanduíches individuais**. É muito mais fácil consumir e processar pequenos sanduíches (chunks) do que tentar comer o pão inteiro de uma vez só.

## Embeddings e Armazenamento Vetorial
Inevitavelmente, você trabalhará com modelos de *embedding* e armazenamento vetorial.
* **O que é:** Basicamente, existem *transformers* rodando para gerar dados vetoriais (números) a partir de texto.
* **Independência de Provedor:** O LangChain oferece interfaces que facilitam a troca de fornecedores. Você não fica preso a um *provider* específico. Você gera *embeddings* facilmente com OpenAI, HuggingFace, etc.

> **Exemplo de Embedding:**
> O modelo transforma uma frase como **"O céu é azul"** em uma sequência numérica complexa que a máquina entende matematicamente, em vez de apenas ler as palavras.

Basicamente, tudo o que você faz em IA (desde *self-attention* até *feed-forward*) é baseado em vetores. Os dados precisam ser vetorizados para fazer sentido dentro do modelo e interagir com os pesos treinados.

## O Poder do Encadeamento e LCEL
O LangChain é poderoso porque não permite apenas executar uma ação isolada, mas sim **encadear ações**.
* **Evolução e Desafios:** De 2023 para 2024, a ferramenta evoluiu muito rápido, o que gerou alguns desafios de compatibilidade (falaremos da arquitetura no site deles posteriormente).

### LCEL (LangChain Expression Language)
Foi introduzido algo chamado **LCEL**. Antigamente, pegar a saída de uma etapa e colocar como entrada na próxima era burocrático.
* **Função:** Agora, com o LCEL, essa transferência é fluida.

> **Exemplo de Encadeamento (Chain):**
> Imagine uma **linha de montagem de automóveis**. O chassi (saída da etapa 1) passa automaticamente para a pintura (entrada da etapa 2), e depois para a montagem do motor (entrada da etapa 3), sem que o operário precise carregar o carro nas costas entre as estações.

## Abstração de Banco de Dados e Memória
* **Nível de Abstração:** O LangChain abstrai os detalhes de baixo nível ("low level"). Você não precisa decorar o SDK específico de cada banco de dados vetorial; a ferramenta gerencia isso para você.
* **Memória:** Recursos nativos para guardar o histórico da conversa conforme a interação ocorre.

### Otimização e Sumarização
Para conversas longas, não precisamos injetar todo o histórico o tempo todo.
* **Sumarização:** Conseguimos resumir a conversa.
* **MapReduce:** Técnicas para processar grandes volumes de chamadas de LLM.

> **Exemplo de Sumarização:**
> Se a conversa fosse uma **longa ata de reunião de 5 horas**, o sistema criaria um **resumo executivo com os 5 pontos principais** para passar para o modelo, economizando processamento e mantendo o foco.

## Resumo dos Principais Recursos Técnicos

### 1. Carregamento e Divisão (Document Loaders)
Capacidade de carregar e processar diversos formatos:
* CSVs, JSON, HTML, Markdown.
* Sites inteiros e documentos PDF.

### 2. Embeddings e Vector Stores
Interface unificada para geração e armazenamento:
* **Geração:** OpenAI, HuggingFace.
* **Bancos Vetoriais:** Pinecone, PGVector (Postgres), Weaviate, FAISS.
* **Busca:** Realização de busca por similaridade semântica.

### 3. Agentes e Ferramentas
* Os agentes utilizam a LLM como um "cérebro" para processar a entrada.
* Eles têm autonomia para **decidir quais ações ou ferramentas executar** com base no pedido.

### 4. Outros Componentes Essenciais
* **Memória e Histórico:** Gestão de contexto.
* **Prompt Templates:** Placeholders e estruturas reutilizáveis de comandos.
* **OutputParsing & Pydantic:** Estruturação e validação das saídas geradas pela IA.
