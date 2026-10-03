import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODBURI")
DB_NAME = os.getenv("DB_NAME", "Master_Note")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not configured in the .env file")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
note_collection = db["Notes"]

