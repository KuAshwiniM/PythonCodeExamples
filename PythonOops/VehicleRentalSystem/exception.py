class InvalidRentalDurationError(ValueError):
    """Raised when the rental duration is invalid (e.g., <= 0)."""
    pass

class VehicleNotFoundError(Exception):
    """Raised when a requested vehicle cannot be found."""
    pass