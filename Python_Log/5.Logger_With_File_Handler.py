# Logger with a file handler
# By default every logger is setup to send log messages to console associated with running program.
# We can change it by configuring a logger with a new handler with a new destination.
# Create a file handler with basicConfig() method and provide file name in the mathod as attribute.

import logging

logger = logging.basicConfig(filename="log.txt", level=logging.DEBUG)

logger = logging.getLogger("user")
logger.setLevel(logging.INFO)

logger.warning("This is WARNING")
logger.error("This is ERROR")
logger.info("This is INFO")
logger.debug("This is DEBUG")
