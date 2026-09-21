
from . import log
logger = log.logging.getLogger("CalculatorTool.converter")


def _validate_numeric(value):
    if not isinstance(value, (int, float)):
        logger.error(f"TypeError: Expected int or float, got {type(value).__name__}")
        raise TypeError(f"Invalid data type: {type(value).__name__}. Must be a number.")


def celsius_to_fahrenheit(celsius):
    _validate_numeric(celsius)
    result = (celsius * 9 / 5) + 32
    logger.info(f"Converted {celsius}°C to {result}°F")
    return result


def fahrenheit_to_celsius(fahrenheit):
    _validate_numeric(fahrenheit)
    result = (fahrenheit - 32) * 5 / 9
    logger.info(f"Converted {fahrenheit}°F to {result}°C")
    return result


def meters_to_feet(meters):
    _validate_numeric(meters)
    if meters < 0:
        logger.error(f"ValueError: Distance cannot be negative ({meters}m).")
        raise ValueError("Distance value cannot be negative.")
    result = meters * 3.28084
    logger.info(f"Converted {meters} meters to {result} feet")
    return result


def meters_to_kilometers(meters):
    _validate_numeric(meters)
    if meters < 0:
        logger.error(f"ValueError: Distance cannot be negative ({meters}m).")
        raise ValueError("Distance value cannot be negative.")
    result = meters / 1000
    logger.info(f"Converted {meters} meters to {result} kilometers")
    return result


def kilometers_to_meters(kilometers):
    _validate_numeric(kilometers)
    if kilometers < 0:
        logger.error(f"ValueError: Distance cannot be negative ({kilometers}km).")
        raise ValueError("Distance value cannot be negative.")
    result = kilometers * 1000
    logger.info(f"Converted {kilometers} kilometers to {result} meters")
    return result
