import re
from typing import List
from collections import Counter

from .models import Product


def get_repeated_characters_amount(string: str) -> int:
    """Get amount of repeated characters in a given string"""

    string = re.sub(r" ", "", string)
    occurences = Counter(string)
    repeated_characters = 0

    for key, value in occurences.items():
        repeated_characters += 1 if value > 1 else 0

    return repeated_characters


def set_products_discounts(products: List[Product]) -> List[Product]:
    pass
