from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["petlove_ai"]
collection = db["products"]

products = list(db["products"].find())
for p in products:
    print(p)
