from chroma_config import get_chroma_client
from chromadb import PersistentClient

client = client = PersistentClient(path="chroma_db")  
print("Collections existentes:", client.list_collections())
