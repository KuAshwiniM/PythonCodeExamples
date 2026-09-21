
from .genericfunction import validate_input
from . import log
logger = log.logging.getLogger('CalculatorTool.arithmetic')

def add(*args):
    validate_input(*args)
    result = args[0]
    for num in args[1:]:
        result += num
    logger.info(f"Addition successful: {' + '.join(map(str, args))} = {result}")
    return result

def sub(*args):
    validate_input(*args)
    result = args[0]
    for num in args[1:]:
        result -= num
    logger.info(f"Subtraction successful: {' - '.join(map(str, args))} = {result}")
    return result

def mul(*args):
    validate_input(*args)
    result = args[0]
    for num in args[1:]:
        result *= num
    logger.info(f"Multiplication successful: {' * '.join(map(str, args))} = {result}")
    return result

def div(a,b):
    validate_input(a, b)
    try:
        if b == 0:
            logger.error("ZeroDivisionError: Attempted division by zero.")
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        raise
    return result        

def percentage(value, percent):
    validate_input(value, percent)
    if percent < 0:
        logger.error(f"InvalidOperationError: Negative percentage requested ({percent}%).")
        raise ValueError("Percentage cannot be negative.")
    result = (value * percent) / 100
    logger.info(f"Percentage calculation successful: {percent}% of {value} = {result}")
    return result