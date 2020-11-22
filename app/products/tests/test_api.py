from unittest import TestCase
from fastapi.encoders import jsonable_encoder

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestUserAPI(TestCase):
    def test_get_products(self):
        response = client.get("/api/products")
        print(response.text)

    def test_create_user(self):
        data = dict(email="sss", password="ddd")
        response = client.post("/api/user/", json=jsonable_encoder(data))
        print(response.text)
