class DartAPIError(Exception):
    """Base exception for DART API errors."""
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

class DartAuthError(DartAPIError):
    """Raised when API key is invalid or missing."""
    pass

class DartLimitError(DartAPIError):
    """Raised when API rate limit is exceeded."""
    pass
