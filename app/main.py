import typing as t

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from products import ProductAPIRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes - api
app.include_router(ProductAPIRouter, prefix="/api/products")
