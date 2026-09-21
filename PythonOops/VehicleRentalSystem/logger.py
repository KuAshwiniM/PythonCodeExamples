import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.FileHandler("vehiclerentalapp.log"),
            logging.StreamHandler() ]
    )
    return logging.getLogger("VehicleRentalApp")

logger = setup_logger()