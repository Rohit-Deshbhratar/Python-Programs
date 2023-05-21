# How to implement default logger in Phython?
# Default logger
# By default it will show CRITICAL, ERROR, WARNING.
# To show all messages uncomment line number 8 -> logging.basicConfig(level=logging.DEBUG)

import logging

# logging.basicConfig(level=logging.DEBUG)

logging.critical("This is CRITICAL")
logging.debug("This is DEBUG")
logging.error("This is ERROR")
logging.info("This is INFO")
logging.warning("This is WARNING")