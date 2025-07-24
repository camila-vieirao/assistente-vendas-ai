#!/bin/bash

# Esperar o Mongo estar pronto
echo "Aguardando o MongoDB iniciar..."
until nc -z mongo 27017; do
  sleep 1
done

echo "Mongo está pronto!"

# Rodar ingestão
echo "Rodando ingestão de produtos..."
python -m petlove_agents.kb_utils.embeddings.ingest_products

# Iniciar a API
echo "Iniciando a API..."
uvicorn api.app:app --host 0.0.0.0 --port 8000
chmod +x entrypoint.sh
