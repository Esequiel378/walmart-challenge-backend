from unittest import TestCase
from fastapi.encoders import jsonable_encoder

from . import client

from products.utils import get_repeated_characters_amount


class TestUserAPI(TestCase):
    def test_repeated_characters_amount(self):

        test_description = "Coche Travel System Tesla"
        expected = 5

        repeated_character = get_repeated_characters_amount(test_description)

        assert expected == repeated_character
