from exception import InvalidRentalDurationError,VehicleNotFoundError
from logger import logger

class Vehicle:
    def __init__(self, vehicle_number: str, brand: str, model: str, rental_price_per_day: float):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        logger.info(f"Initialized Vehicle: {self.brand} {self.model} ({self.vehicle_number})")

    @staticmethod
    def validate_rental_duration(days: int) -> bool:
        """Validates that the rental duration is greater than zero."""
        if not isinstance(days, int) or days <= 0:
            return False
        return True

    def calculate_rent(self, days: int) -> float:
        """Calculates total rent based on number of days."""
        if not self.validate_rental_duration(days):
            logger.error(f"Invalid rental duration attempted: {days} days")
            raise InvalidRentalDurationError("Rental duration must be an integer greater than zero.")
        
        total_rent = days * self.rental_price_per_day
        logger.info(f"Calculated rent for {self.vehicle_number} ({days} days): ${total_rent:.2f}")
        return total_rent


class Car(Vehicle):
    def __init__(self, vehicle_number: str, brand: str, model: str, rental_price_per_day: float, seats: int):
        super().__init__(vehicle_number, brand, model, rental_price_per_day)
        self.seats = seats
        logger.info(f"Added Car specific attribute - Seats: {self.seats}")


class Bike(Vehicle):
    def __init__(self, vehicle_number: str, brand: str, model: str, rental_price_per_day: float, engine_capacity: int):
        super().__init__(vehicle_number, brand, model, rental_price_per_day)
        self.engine_capacity = engine_capacity
        logger.info(f"Added Bike specific attribute - Engine Capacity: {self.engine_capacity}cc")