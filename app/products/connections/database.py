from typing import Optional, List

from fastapi import Depends
from database import get_database

from products.models import Product

from .exceptions import EntryDoesNotExist


class DatabaseConnection:
    def __init__(self, db=Depends(get_database)):
        self.collection = db["products"]

        # create index to perfom search
        self.collection.create_index(
            [("brand", "text"), ("description", "text")],
        )

    def get_products(self, search: Optional[str] = None) -> List[Product]:
        """query all products in database and return a list"""

        if not search is None:
            # qs = self.collection.find(
            # {"$text": {"$search": search, "$caseSensitive": False}}, {"_id": False},
            # )
            qs = self.collection.find(
                {"description": {"$regex": f".*{search}.*"}}, {"_id": False}
            )

        else:
            qs = products_collection.find({}, {"_id": False})

        return list(qs)

    def get_product(self, id: int) -> Product:
        """get a product from a given id"""

        post = self.collection.find_one({"id": id}, {"_id": False})

        if not post:
            raise EntryDoesNotExist(id)

        return post

    def add_product(self, product: Product):
        """Add a given product to database"""

        self.collection.insert_one(product.dict())
