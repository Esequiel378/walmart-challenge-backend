from typing import Optional, List

from fastapi import Depends
from database import get_database

from products.models import Product

from .exceptions import EntryDoesNotExist

class ProductsDatabaseConnection:
    def __init__(self, db=Depends(get_database)):
        self.collection = db["products"]

        # create index to perfom search
        self.collection.create_index([("brand", "text"), ("description", "text")],)

    def list(self) -> List[Product]:
        """query all products in database and return a list"""

        qs = self.collection.find({}, {"_id": False})

        return list(qs)

    def search(self, query: str) -> List[Product]:
        """Search products by brand or description"""

        print(query)

        qs = self.collection.find(
            {
                "$or": [
                    {"brand": {"$regex": query, "$options": "i"}},
                    {"description": {"$regex": query, "$options": "i"}},
                ]
            },
            {"_id": False},
        )

        return list(qs)

    def get(self, id: int) -> Product:
        """get a product from a given id"""

        post = self.collection.find_one({"id": id}, {"_id": False})

        if not post:
            raise EntryDoesNotExist(id)

        return post

    def create(self, product: Product):
        """Add a given product to database"""

        self.collection.insert_one(product.dict())

    def bulk_create(self, products: List[Product]):
        """Add a given list of products to database"""

        entries = [product.__dict__ for product in products]

        self.collection.insert_many(entries)
