from pydantic import BaseModel

class Product(BaseModel):
    id: int
    brand: str
    description: str
    image: str
    price: int


class Discount(BaseModel):
    brand: str
    threshold: str
    discount: int
