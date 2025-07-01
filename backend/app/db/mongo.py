from pymongo import MongoClient
import os

mongo_url = os.getenv("MONGO_URL", "mongodb://mongo:27017")  # 👈 usa el nombre del contenedor, no localhost
client = MongoClient(mongo_url)
db = client["inmax_db"]