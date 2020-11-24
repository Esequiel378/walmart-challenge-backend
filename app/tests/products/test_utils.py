from tests import client
import pytest

from products.models import Product, ProductWithDiscountPromotion
from products.utils import (
    get_product_discount_promotion,
    get_products_discount_promotion,
    get_repeated_characters_amount,
)


class TestProductUtils:
    @pytest.mark.parametrize(
        "description,expected", [
           ("Coche Travel System Tesla", 5),
           ("Microondas 120W"", 1),
           ("Cargador Smart Phone USB", 4),
        ]
    )
    def test_repeated_characters_amount(self, description, expected):

        repeated_character = get_repeated_characters_amount(test_description)

        assert expected == repeated_character

    def test_get_product_discount_promotion(self):

        product = {
            "id": 999,
            "brand": "Marca1",
            "description": "Coche Travel System Tesla",
            "image": "www.lider.cl/catalogo/images/catalogo_no_photo.jpg",
            "price": 80000,
        }
        expected_discount = 50

        product_with_discount = get_product_discount_promotion(product)

        assert isinstance(product_with_discount, ProductWithDiscountPromotion)
        assert product_with_discount.discount == expected_discount

    def test_get_products_discount_promotion(self):

        products = [
            {
                "id": 4,
                "brand": "Marca2",
                "description": "Refrigerador",
                "image": "www.lider.cl/catalogo/images/catalogo_no_photo.jpg",
                "price": 20000,
            },
            {
                "id": 3,
                "brand": "Marca1",
                "description": "Horno Gas Premium",
                "image": "www.lider.cl/catalogo/images/catalogo_no_photo.jpg",
                "price": 30000,
            },
        ]
        expected_discounts = [20, 30]

        products_with_discount = get_products_discount_promotion(products)

        assert isinstance(products_with_discount, list)

        for product_with_discount, expected_discount in zip(
            products_with_discount, expected_discounts
        ):
            assert product_with_discount.discount == expected_discount
