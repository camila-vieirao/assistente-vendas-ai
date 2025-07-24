FROM python:3.11-slim

WORKDIR /app

# Copiar tudo da raiz do projeto
COPY . .

# Instalar dependências
RUN pip install --upgrade pip
RUN pip install -r api/requirements.txt

# Tornar script executável
RUN chmod +x entrypoint.sh

# Porta da API
EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
