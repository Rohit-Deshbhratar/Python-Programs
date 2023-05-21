# Logger with built in handler and custom formatter
# Refer program "3.Logger_With_Built_In_Handler_Custom_Formatter.py"
# In this program we will create a logger with the same settings by using 
# the basicConfig() method as well with appropriate arguments.

import logging

logger = logging.getLogger("user")
logging.basicConfig(handlers=[logging.StreamHandler()],
                    format="%(asctime)s - %(name)a - %(levelname)s - %(message)s",
                    level=logging.INFO)

logger.critical("This is CRITICAL")
logger.debug("This is DEBUG")
logger.error("This is ERROR")
logger.info("This is INFO")
logger.warning("This is WARNING")
