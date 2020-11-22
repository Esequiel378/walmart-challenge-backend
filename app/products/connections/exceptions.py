class BaseConnectionException(Exception):
    """Global exception class for connections."""

    def __init__(self, message=None):
        super().__init__(message)


class EntryDoesNotExist(BaseConnectionException):
    """Entry not found error."""

    def __init__(self, entry):
        super().__init__(f"Entry not found {str(entry)}")
