import logging

def setup_logger():
    """Initializes and returns a system logger configuration."""
    logger = logging.getLogger("Super30Platform")
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler("super30_platform.log")
        
        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.DEBUG)
        
        # Create formatters
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(log_format)
        f_handler.setFormatter(log_format)
        
        # Add to logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        
    return logger

logger = setup_logger()