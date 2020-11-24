import unicodedata


def remove_accents(string: str) -> str:
    """Remove wired characters from string"""

    return "".join(
        c for c in unicodedata.normalize("NFKD", string) if not unicodedata.combining(c)
    )


def contains(container: str, string: str) -> bool:
    """Check if container string contains a given string."""

    container = remove_accents(container).lower()
    string = remove_accents(string).lower()

    return string in container

