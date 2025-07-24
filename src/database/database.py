from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["petlove_ai"]
collection = db["products"]

with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

    result = collection.insert_many(products)
    print(f"{len(result.inserted_ids)} produtos inseridos com sucesso!")

#verificar produtos

#products = list(db["products"].find())
#for p in products:
#    print(p)
