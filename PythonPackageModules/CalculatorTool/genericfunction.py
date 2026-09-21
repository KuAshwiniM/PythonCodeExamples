from . import log
logger = log.logging.getLogger('CalculatorTool.genericfunction')
def validate_input(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            logger.error(f"TypeError: Expected int or float, got {type(arg).__name__}")
            raise TypeError(f"Invalid data type: {type(arg).__name__}. Only numbers are allowed.")
        else:
            logger.info(f"Input validation successful: {arg} is a valid number.")