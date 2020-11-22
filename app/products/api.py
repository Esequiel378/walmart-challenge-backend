from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from .models import Product
from .connections import DatabaseConnection

import typing as t


router = InferringRouter()


@cbv(router)
class ProductAPI:

    db: DatabaseConnection = Depends(DatabaseConnection)

    @router.get("/")
    async def products(self, search: t.Optional[str] = None) -> t.List[Product]:
        """List all products"""

        return self.db.get_products(search)

    @router.get("/{id}")
    async def products(self, id: int) -> Product:
        """Get product by id"""

        return self.db.get_product(id)

    @router.post("/")
    async def add_product(self, product: Product):
        """Create a new product entry"""

        self.db.add_product(product)

        return {"message": "success"}
