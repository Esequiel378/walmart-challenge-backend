import typing as t

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Discount, Product
from database import get_products

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> t.List[Product]:
    qs = get_products()
    return list(qs)


@app.get("/products")
async def products() -> t.List[Product]:
    return []


@app.get("/products/{id}")
async def products(id: int) -> Product:
    return Product(id=id, brand="breadm", description="asd", image="asd", price=123123)
