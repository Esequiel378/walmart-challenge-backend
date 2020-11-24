import re
from typing import List
from collections import Counter

from .models import Product, ProductWithDiscountPromotion


def get_repeated_characters_amount(string: str) -> int:
    """Get amount of repeated characters in a given string"""

    string = re.sub(r" ", "", string)
    occurences = Counter(string)
    repeated_characters = 0

    for key, value in occurences.items():
        repeated_characters += 1 if value > 1 else 0

    return repeated_characters


def get_product_discount_promotion(product: Product) -> ProductWithDiscountPromotion:
    """Get the product discount promotion from a given product"""

    discount = min(get_repeated_characters_amount(product.get("description")), 5) * 10
    product_with_discount = ProductWithDiscountPromotion(**product, discount=discount)

    return product_with_discount


def get_products_discount_promotion(
    products: List[Product],
) -> List[ProductWithDiscountPromotion]:
    """Get the product discount promotion from a given list of product"""

    products_with_discounts = [
        get_product_discount_promotion(product) for product in products
    ]

    return products_with_discounts
