from pymongo import MongoClient

import os

DATABASE_URI = os.environ.get("DATABASE_URI")
DATABASE_NAME = os.environ.get("DATABASE_NAME")


def get_database():
    """Yield a products collections instance"""

    client = MongoClient(DATABASE_URI)
    db = client[DATABASE_NAME]

    try:
        yield db
    finally:
        client.close()
