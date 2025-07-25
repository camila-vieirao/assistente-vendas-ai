# 🐶 Assistente de Vendas Petlove (AI)

Este projeto é uma API que recomenda produtos com base em uma conversa, utilizando modelos de linguagem e um banco vetorial.

## 🚀 Como rodar com Docker

### 1. Clone o projeto

```bash
git clone https://github.com/camila-vieirao/assistente-vendas-ai.git
cd assistente-vendas-ai
````

### 2. Configure o ambiente

Crie um arquivo `.env` com base no modelo `.env.example`.

Edite o `.env` e preencha com seu `GROQ_API_KEY`.
> Manter "`OPENAI_API_KEY=dummy`", por conta de um bug do crewai.

### 3. Rode tudo com Docker Compose

inicie a engine do Docker através do Docker Desktop, e após isso rode o seguinte comando:

```bash
docker-compose up --build
```

Esse comando irá:

* Baixar e subir o MongoDB
* Instalar as dependências da API
* Popular o banco de dados
* Inserir os dados no Chroma
* Subir a API em `http://localhost:8000`

---

## 🧪 Como testar

Abra: [http://localhost:8000/docs](http://localhost:8000/docs)

Use o endpoint `/api/question-and-answer` com o seguinte corpo:

```json
{
  "message": "eu gostaria de comprar brinquedo para cachorro",
  "role": "user",
  "conversation_id": "<id>"
}
```

---

## 🛠 Tecnologias

* 🧠 LLM (Groq)
* 🔢 Embeddings (HuggingFace)
* 🧬 MongoDB
* ⚡ FastAPI
* 🧭 ChromaDB
* 🐳 Docker

---

## Demonstração

![](steps.gif)
