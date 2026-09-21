from .genericfunction import validate_input
from . import log
logger = log.logging.getLogger('CalculatorTool.statistics')

def mean(*args):
    validate_input(*args)
    result = sum(args) / len(args)
    logger.info(f"Mean calculation successful: mean({', '.join(map(str, args))}) = {result}")
    return result
