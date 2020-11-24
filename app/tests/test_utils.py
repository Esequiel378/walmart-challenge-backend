import pytest

from utils import contains, remove_accents
from tests import client


class TestUtils:
    def test_remove_accents(self):
        string = "This is â wíred stríng"
        expected = "This is a wired string"

        result = remove_accents(string)

        assert result == expected

    @pytest.mark.parametrize(
        "container,string,expected",
        [
            ("This is a container string", "container", True),
            ("I like to eat apples", "banana", False),
        ],
    )
    def test_contains(self, container, string, expected):

        result = contains(container, string)

        assert result == expected
