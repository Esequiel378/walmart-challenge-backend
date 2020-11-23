from unittest import TestCase
from fastapi.encoders import jsonable_encoder

from . import client


class TestUserAPI(TestCase):
    def test_get_products(self):
        response = client.get("/api/products")
        import pdb; pdb.set_trace()

        data = list()

        assert type(data) == list

    def test_create_user(self):
        data = dict(email="sss", password="ddd")
        response = client.post("/api/user/", json=jsonable_encoder(data))
        print(response.text)
