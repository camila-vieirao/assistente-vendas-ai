from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from chromadb import PersistentClient 
from sentence_transformers import SentenceTransformer
import os
from petlove_agents.kb_utils.embeddings.chroma_config import get_chroma_client

class ChromaSearchInput(BaseModel):
    query: str = Field(
        ..., 
        description="A consulta de busca a ser executada. Pode ser uma pergunta ou frase descritiva que represente a intenção do usuário."
    )

    top: int = Field(
        default=3, 
        description="Quantidade de resultados mais relevantes que devem ser retornados. Use valores menores para respostas objetivas, maiores para consultas mais amplas."
    )

    
    @classmethod
    def validate_input(cls, values):
        query = values.get("query")
        top = values.get("top", 3)

        if isinstance(query, dict):
            query = query.get("description") or query.get("value") or str(query)
        if isinstance(top, dict):
            top = int(top.get("description") or top.get("value") or 3)

        values["query"] = query
        values["top"] = top
        return values

    # Isso executa antes da validação Pydantic
    @classmethod
    def model_validate(cls, data):
        return super().model_validate(cls.validate_input(data))

class ChromaSearchTool(BaseTool):
    name: str = "Busca por produtos"
    description: str = (
        "Busca vetorial que retorna produtos mais relevantes de pets com base na pergunta do usuário. Use esta ferramenta quando precisar pesquisar em documentos indexados"
    )
    args_schema: Type[BaseModel] = ChromaSearchInput

    def _run(self, query: str, top: int = 3, **kwargs) -> str:
        try:
            if isinstance(query, dict):
                query = query.get("description") or query.get("value") or str(query)
            if isinstance(top, dict):
                top = int(top.get("description") or top.get("value") or 3)

            chroma_client = get_chroma_client()
            collection = chroma_client.get_collection(name="product_embeddings")

            #vetorizacao da query
            model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", trust_remote_code=True)
            embeddings = model.encode(
                query,
                normalize_embeddings=True
            ) 

            results = collection.query(query_embeddings=[embeddings], n_results=min(top, 3), include=["documents", "metadatas", "distances"])

            formatted_results = []
            for i in range(len(results["documents"][0])):
                formatted_result = {
                    "score": results["distances"][0][i],
                    "document": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i]
                }
                formatted_results.append(formatted_result)

            return str(formatted_results)


        except Exception as e:
            return f"erro na busca no chroma: {str(e)}" 