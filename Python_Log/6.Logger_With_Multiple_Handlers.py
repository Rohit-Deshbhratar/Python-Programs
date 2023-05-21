# Using loggers with multiple handlers
# Create two handlers which will be the instance of StreamHandlers and FileHandlers classes
# Create 2 separate formatters for each handlers. Do not include time formatter in console handler.
# Create two separate logging levels for each handlers.

import logging

logger = logging.getLogger("USER")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("multiple-handler.log")

# Setting logging levels at handlers level
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

# Creating separate formatter for two handlers  
console_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Adding formatters to the handlers
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Adding handlers to the loggers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.warning("This is WARNING")
logger.error("This is ERROR")
logger.info("This is INFO")
logger.debug("This is DEBUG")