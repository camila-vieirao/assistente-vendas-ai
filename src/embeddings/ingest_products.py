from pymongo import MongoClient
import json
from chroma_config import get_or_create_collection
from vectorizer import embed_texts

mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["petlove_ai"]
products = db["products"].find()

# produtos do mongo
product_list = list(products)
texts = [p["description"] for p in product_list]
ids = [str(p["_id"]) for p in product_list]
metadatas = [
    {
        "name": p["name"],
        "price": p["price"],
        "url": p.get("product_url") or p.get("link"),
        "category": p.get("category")
    }
    for p in product_list
]

print("Textos extraídos do Mongo:", len(texts))
embeddings = embed_texts(texts)

# inserir no chroma
collection = get_or_create_collection()

collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=ids,
    metadatas=metadatas
)

print(f"Inseridos {len(ids)} produtos no Chroma.")
