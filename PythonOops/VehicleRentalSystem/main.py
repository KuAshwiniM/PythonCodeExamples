from vehicle import Vehicle,Car, Bike
from exception import InvalidRentalDurationError,VehicleNotFoundError
from logger import logger

def main():
    logger.info("Starting Vehicle Rental System Demonstration...")

    # Create 2 cars and 2 bikes
    car1 = Car("CAR-101", "Toyota", "Camry", 50.0, seats=5)
    car2 = Car("CAR-102", "Honda", "Civic", 40.0, seats=5)
    
    bike1 = Bike("BIKE-201", "Yamaha", "MT-07", 25.0, engine_capacity=689)
    bike2 = Bike("BIKE-202", "Kawasaki", "Ninja 300", 30.0, engine_capacity=296)

    fleet = [car1, car2, bike1, bike2]

    # Demonstrate normal calculation
    rental_days = 4
    logger.info(f"\n--- Processing Rentals for {rental_days} Days ---")
    for v in fleet:
        try:
            cost = v.calculate_rent(rental_days)
            print(f"Vehicle: {v.brand} {v.model} [{v.vehicle_number}] -> Rent for {rental_days} days: ${cost:.2f}")
        except InvalidRentalDurationError as e:
            print(f"Error for {v.vehicle_number}: {e}")

    # Demonstrate static method validation & exception handling with invalid input
    logger.info("\n--- Testing Invalid Rental Duration ---")
    invalid_days = 0
    test_vehicle = car1
    
    print(f"Is rental duration {invalid_days} valid? {Vehicle.Car.validate_rental_duration(invalid_days) if hasattr(Vehicle, 'Car') else test_vehicle.validate_rental_duration(invalid_days)}")
    
    try:
        test_vehicle.calculate_rent(invalid_days)
    except InvalidRentalDurationError as e:
        logger.warning(f"Caught expected exception: {e}")
        print(f"Successfully caught validation error: {e}")

    logger.info("Rental System Demonstration Completed.")

if __name__ == "__main__":
    main()