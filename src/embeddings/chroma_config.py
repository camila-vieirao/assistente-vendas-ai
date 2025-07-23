import chromadb

def get_chroma_client():
    return chromadb.Client()

def get_or_create_collection(name="product_embeddings"):
    client = get_chroma_client()
    return client.get_or_create_collection(name=name)
