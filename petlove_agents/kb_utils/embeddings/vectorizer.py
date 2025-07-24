from sentence_transformers import SentenceTransformer

model = SentenceTransformer("jinaai/jina-embeddings-v3", trust_remote_code=True)

def embed_texts(texts: list[str]) -> list[list[float]]:
    if not texts:
        return []

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    print(f"Embeddings gerados: {len(embeddings)} vetores de {len(embeddings[0])} dimensões")
    return embeddings
