import chromadb
from chromadb.config import Settings

persist_dir = "db"

def get_chroma_client():
    return chromadb.PersistentClient(path="chroma_db")

def get_or_create_collection(name="product_embeddings"):
    client = get_chroma_client()
    return client.get_or_create_collection(name=name)
