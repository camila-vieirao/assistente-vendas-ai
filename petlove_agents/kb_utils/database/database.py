from pymongo import MongoClient
import json
import os

def populate_products_if_needed():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["petlove_ai"]
    collection = db["products"]

    # Só popula se estiver vazio
    if collection.count_documents({}) == 0:
        file_path = os.path.join(os.path.dirname(__file__), "products.json")

        with open(file_path, "r", encoding="utf-8") as f:
            products = json.load(f)

        result = collection.insert_many(products)
        print(f"{len(result.inserted_ids)} produtos inseridos com sucesso!")
    else:
        print("Produtos já presentes no MongoDB. Nenhuma inserção necessária.")
