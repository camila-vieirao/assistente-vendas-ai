import chromadb
from chromadb.config import Settings
import os


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "chroma_db")
)


def get_chroma_client():
    return chromadb.PersistentClient(path=BASE_DIR)

def get_or_create_collection(name="product_embeddings"):
    client = get_chroma_client()
    return client.get_or_create_collection(name=name)
