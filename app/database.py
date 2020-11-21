from pymongo import MongoClient
from bson import ObjectId

from typing import List
import os

DATABASE_URI = os.environ.get("DATABASE_URI")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

client = MongoClient(DATABASE_URI)

db = client[DATABASE_NAME]

collection = db["products"]


def get_products():
    return collection.find()
