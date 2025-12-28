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

---

# Iniciando com Sumarização: Contexto e Necessidade

## O Problema: Acúmulo de Tokens e Stateless
Para entender a importância da sumarização, precisamos primeiro entender como as LLMs funcionam em conversas longas:
* **Natureza Stateless:** Por padrão, a LLM não tem memória. Ela não guarda o estado da conversa anterior.
* **O Acúmulo:** Para manter a coerência ("Lembrar do que foi dito"), você precisa re-enviar todo o histórico a cada nova interação (Interação 1 + Interação 2 + Interação 3...).
* **A Consequência:** O texto de entrada (input) cresce exponencialmente, consumindo mais *tokens* a cada rodada.

## A Questão da Janela de Contexto (Context Window)
Antigamente, o problema era o limite técnico (a janela "estoura" e você perde mensagens antigas). Hoje, com modelos modernos (o instrutor cita hipoteticamente um "GPT-5"), temos janelas de 1 milhão de tokens e saídas de 128k tokens.
* **A pergunta:** *Se a janela é gigante, por que eu preciso sumarizar?*

## Os Três Pilares da Decisão (Por que usar?)
Mesmo com janelas de contexto infinitas, a sumarização é vital por três motivos, especialmente pensando em **Larga Escala**:

1.  **Custo ($$):** Você paga por token processado. Enviar um histórico gigante de 4 anos de conversa toda vez que o usuário diz "Oi" é financeiramente inviável em escala.
2.  **Latência (Performance):** Quanto mais tokens a IA precisa ler e processar, mais lenta é a resposta. Memória e poder computacional são recursos finitos.
3.  **Necessidade Real:** Muitas vezes, para responder à pergunta atual, a IA não precisa ler cada palavra dita há meses atrás; ela precisa apenas do contexto principal.

> **Exemplo Prático de Atendimento ao Cliente:**
> Imagine um cliente que interage com a empresa desde **janeiro de 2026** e volta a chamar em **2030**.
> Não faz sentido carregar e processar o histórico literal de 4 anos (milhares de mensagens) para resolver um problema atual. O que você precisa é de um **resumo** dos eventos principais desse cliente.

## O Que é a Sumarização na Prática?
A sumarização é a técnica de comprimir o histórico:
* **Perda:** Você perde o "palavra por palavra" (o texto exato).
* **Ganho:** Você mantém o **contexto**, as **nuances** e os **dados importantes**.
Isso permite manter a inteligência da aplicação sem inflar o custo e a latência. Como isso virou padrão de mercado, o **LangChain** já possui abstrações prontas para lidar com isso.

---

# Agentes de IA e o Framework ReAct

## O Que São Agentes no LangChain?
No ecossistema do LangChain, é possível criar agentes de forma nativa.
* **Agentes Simples:** O LangChain "puro" é excelente para criar agentes que executam tarefas específicas sem a necessidade de frameworks complexos adicionais.
* **Aplicações Agênticas Complexas:** Para arquiteturas que envolvem múltiplos agentes conversando entre si, ferramentas como o **LangGraph** são mais indicadas para a orquestração.

## A Arquitetura de um Agente
Diferente de um software tradicional (que tem um *entry point* -> regras de negócio fixas -> saída), o Agente de IA funciona de forma diferente:
1.  **O "Cérebro" é a LLM:** O centro do software é o modelo de linguagem.
2.  **Tomada de Decisão:** Ele recebe uma instrução e **decide** qual caminho tomar (ex: sumarizar um texto, consultar um banco de dados, transformar dados em JSON ou buscar na internet).

### Componentes Essenciais
Para um agente funcionar, ele precisa de três pilares:
* **Prompt:** As instruções de como ele deve raciocinar e se comportar (persona).
* **Ferramentas (Tools):** As habilidades que ele possui (ex: função de busca, calculadora, acesso a API).
* **Recursos (Resources/MCP):** Fontes de dados e protocolos de contexto que ele pode acessar para obter informações.

---

## O Conceito ReAct (Reason + Act)
O padrão mais conhecido para agentes no LangChain é o **ReAct**. O nome vem da fusão de **Re**asoning (Raciocínio) e **Act**ing (Ação).

Não é apenas "reagir"; é uma **estrutura de pensamento cíclica**. O agente repete o seguinte loop até resolver o problema:
1.  **Thought (Pensar):** O agente analisa o pedido e planeja o próximo passo.
2.  **Action (Agir):** Ele executa uma ação baseada no pensamento (ex: usar uma ferramenta).
3.  **Observation (Observar):** Ele lê o resultado dessa ação.
4.  **Repeat:** Ele usa a observação para gerar um novo pensamento.

---

## Exemplo Prático do Ciclo ReAct
Imagine que o usuário pergunte: **"Qual a população do Brasil e a densidade demográfica?"**

### Ciclo 1
* **Thought:** Preciso da população atual e da área territorial.
* **Action:** *Busca no Google:* "População Brasil 2024".
* **Observation:** Encontrei "216 milhões de habitantes".

### Ciclo 2
* **Thought:** Agora tenho a população, preciso da área.
* **Action:** *Busca no Google:* "Área territorial Brasil km²".
* **Observation:** Encontrei "8.515.767 km²".

### Ciclo 3
* **Thought:** Tenho os dois dados. Agora preciso calcular a densidade (População / Área).
* **Action:** *Executar Cálculo* (216.000.000 / 8.515.767).
* **Observation:** Resultado é aprox. 25.37.

### Final Answer
* **Resposta:** "O Brasil tem aproximadamente 216 milhões de habitantes e uma densidade de 25.4 habitantes por km²."

Essa estrutura de **raciocínio explícito** é o que permite aos agentes resolverem problemas complexos passo a passo, em vez de tentar adivinhar tudo de uma vez.

---

# Introdução ao Gerenciamento de Memória em IA

## 1. O que é "Memória" neste contexto?
Antes de tudo, é vital desmistificar o termo. Quando falamos de memória em Agentes de IA e LLMs:
* **Não é:** Memória RAM, VRAM (GPU) ou espaço de disco do servidor.
* **É:** A capacidade de **guardar o contexto** e o conteúdo histórico das interações para que o modelo entenda a continuidade da conversa.

## 2. O Desafio: A Natureza Stateless
Os LLMs (como GPT, Claude, Llama) são **stateless** (sem estado).
* **O Problema:** Eles não "lembram" do que você falou há 10 segundos. Cada interação é nova.
* **A Solução:** Para manter uma conversa coerente, você (o desenvolvedor) precisa reenviar **100% do histórico** de mensagens anteriores junto com a nova pergunta a cada rodada.

> **Nota Técnica:** O modelo possui uma memória interna (pesos treinados) e caches de baixo nível, mas isso é da arquitetura dele. O nosso foco aqui é o **histórico de conversação**.

---

## 3. Tipos de Memória: Curto Prazo vs. Longo Prazo

Podemos dividir o gerenciamento desse histórico em duas categorias principais:

### Memória de Curto Prazo (Short-Term)
* **Definição:** É o contexto mantido apenas **durante uma transação** ou sessão de conversa específica.
* **Funcionamento:** Existe enquanto a operação está ativa.
* **Armazenamento:** Variáveis em memória, Cache (Redis) ou Banco de Dados Temporário.

### Memória de Longo Prazo (Long-Term)
* **Definição:** O histórico persistente que sobrevive dias, meses ou anos (ex: histórico de atendimento de um cliente).
* **Armazenamento:** Obrigatoriamente em **Banco de Dados** persistente.
* **Objetivo:** Permitir restaurar o contexto de onde parou ou analisar comportamentos passados.

---

## 4. O Problema do Histórico Infinito
Conforme o tempo passa, o histórico (chats, e-mails, transcrições) torna-se gigantesco. Tentar enviar **tudo** para a IA gera problemas:

1.  **Custo e Limites:** Enviar terabytes de texto estoura o limite de tokens (*Context Window*) e custa caro.
2.  **Qualidade (Alucinação):** O instrutor destaca um ponto crucial: **"Mais informação nem sempre é melhor"**.
    * Passar um histórico gigante e desnecessário pode gerar ambiguidade e fazer a IA alucinar, similar ao que ocorre quando damos exemplos ruins em *Few-Shot Prompting*.

## 5. Estratégias de Solução
Para lidar com o volume de dados, usamos estratégias como:
* **Restauração Parcial:** Carregar apenas as últimas mensagens.
* **Sumarização:** Compactar o histórico antigo em resumos, mantendo o contexto sem gastar todos os tokens.

## 6. O Papel do LangChain
Como a IA é uma área nova ("uma criança" comparada à engenharia de software tradicional), os padrões ainda estão se formando. O **LangChain** entra como a ferramenta que facilita:
* Carregar mensagens antigas.
* Gerenciar o envio para a LLM.
* Implementar estratégias de memória de forma simplificada.
