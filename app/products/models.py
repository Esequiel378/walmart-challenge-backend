from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    brand: str
    description: str
    image: str
    price: int


class ProductWithDiscountPromotion(Product):
    discount: int
