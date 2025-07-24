## 🐶 Assistente de Vendas com IA - PetLove

Um projeto de inteligência artificial baseado em RAG (Retrieval-Augmented Generation) que ajuda clientes a encontrar produtos de pets respondendo perguntas com base em uma base de dados real.

### 🧠 Tecnologias

* 🐍 Python 3.13.3
* 💾 ChromaDB (vetores)
* 📦 MongoDB (documentos)
* 🔤 Jina Embeddings v3 (modelo de vetorização)
* 🔤 Meta-Llama-3.1-8B-Instruct (modelo de nlp)
* 🤖 CrewAI (orquestração de agentes)

---

## ⚙️ Pré-requisitos

* Python 3.13.3
* MongoDB rodando localmente (padrão: `mongodb://localhost:27017`)

---

## 📥 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/camila-vieirao/assistente-vendas-ai.git
cd assistente-vendas-ai
cd petlove_agents
```

2. Dependencias:

```bash
crewai install
```
---

## 🧪 Configuração e Ingestão dos Dados

1. Certifique-se de que o MongoDB está rodando localmente.

2. Insira os dados no MongoDB:

```bash
python src/database/database.py
```

Esse script faz:

* Carregamento do arquivo `src/database/products.json`.
* Armazenamento dos produtos no MongoDB.

Após inserir os dados no MongoDB:

```bash
python src/embeddings/ingest_products.py
```

Esse script faz:

* Vetorização com `jina-embeddings-v3`.
* Armazenamento dos vetores no banco Chroma local (`chroma_db/`).

---

## 💬 Como rodar o assistente (em breve)

O agente será criado com CrewAI e ficará em `src/crewai/petlove-agents/`.

```bash
python src/crewai/petlove-agents/main.py
```

*(Ainda em desenvolvimento!)*

