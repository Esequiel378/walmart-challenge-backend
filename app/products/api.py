from typing import Optional, List

from fastapi import Depends, HTTPException
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv

from . import utils

from .connections import ProductsDatabaseConnection
from .connections.exceptions import EntryDoesNotExist
from .models import Product, ProductWithDiscountPromotion


router = InferringRouter()


@cbv(router)
class ProductAPI:
    """Products endpoints"""

    db: ProductsDatabaseConnection = Depends(ProductsDatabaseConnection)

    @router.get("/")
    async def list(self) -> List[ProductWithDiscountPromotion]:
        """List all products"""

        products = self.db.list()

        products_with_discounts = utils.get_products_discount_promotion(products)

        return products_with_discounts

    @router.get("/search")
    async def search(self, query: str) -> List[ProductWithDiscountPromotion]:
        """Search products by brand or description"""

        products = self.db.search(query)

        products_with_discounts = utils.get_products_discount_promotion(products)

        return products_with_discounts

    @router.get("/{id}")
    async def get(self, id: int) -> ProductWithDiscountPromotion:
        """Get product by id"""

        try:
            product_entry = self.db.get(id)
        except EntryDoesNotExist as e:
            raise HTTPException(status_code=404, detail=str(e))

        product_with_discount = utils.get_product_discount_promotion(product_entry)

        return product_with_discount

    @router.post("/", status_code=201)
    async def create(self, product: Product):
        """Create a new product entry"""

        self.db.create(product)

        return {"message": "succes"}

    @router.post("/bulk/create/", status_code=201)
    async def bulk_create(
        self, product: List[Product]
    ) -> List[ProductWithDiscountPromotion]:
        """Bulk product creation"""

        self.db.bulk_create(product)

        return {"message": "succes"}

