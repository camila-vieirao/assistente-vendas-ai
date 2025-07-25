FROM python:3.11-slim

WORKDIR /app

# Copiar tudo da raiz do projeto
COPY . .

# Instalar dependências
RUN pip install --upgrade pip
RUN pip install -r api/requirements.txt

# Tornar script executável
RUN apt-get update && apt-get install -y dos2unix netcat-openbsd && \
    dos2unix entrypoint.sh && \
    chmod +x entrypoint.sh

# Porta da API
EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
