import json

from utils import contains
from tests import client


class TestProductAPI:
    def test_list(self):
        response = client.get("/api/products/")

        products = json.loads(response.text)

        assert type(products) == list

    def test_search(self):
        search_query = "telev"
        response = client.get(f"/api/products/search?query={search_query}")

        products = json.loads(response.text)

        for product in products:
            assert contains(product.get("brand"), search_query) or contains(
                product.get("description"), search_query
            )

    def test_get(self):
        expected_id = 1

        response = client.get(f"/api/products/{expected_id}")

        product = json.loads(response.text)

        assert type(product) == dict
        assert product.get("id") == expected_id

    def test_get_unhappy_path(self):
        expected_id = -1

        response = client.get(f"/api/products/{expected_id}")

        product = json.loads(response.text)

        assert type(product) == dict
        assert product == {"detail": f"Entry #{expected_id} not found."}

    def test_create(self):

        product = json.dumps(
            {
                "id": 999,
                "brand": "Marca1",
                "description": "Televisión 54",
                "image": "www.lider.cl/catalogo/images/catalogo_no_photo.jpg",
                "price": 80000,
            }
        )

        response = client.post("/api/products/", data=product)

        result = json.loads(response.text)

        assert result == {"message": "succes"}
