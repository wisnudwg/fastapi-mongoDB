from pymongo import MongoClient
import src.config as config
print(config.MONGO_URI)
client = MongoClient(config.MONGO_URI)

db = client.todo_db

collection_name = db["todo_collection"]