import re
from typing import List
from collections import Counter

from .models import Product


def get_repeted_characters_amount(string: str) -> int:

    string = re.sub(r" ", "", string)
    occurences = Counter(string)
    repeated_character = 0

    for key, value in occurences.items():
        if value > 1:
            repeated_character += 1

    return repeated_character


def set_products_discounts(products: List[Product]) -> List[Product]:
    pass
