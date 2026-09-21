import logging

# Configure global logging settings
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="calculatorlogging.log",  # If omitted, logs stream to console (stderr)
    filemode="w"         # 'w' to overwrite each run; 'a' to append (default)
)