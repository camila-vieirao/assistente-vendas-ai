from chroma_config import get_chroma_client

client = get_chroma_client()
print("Collections existentes:", client.list_collections())
