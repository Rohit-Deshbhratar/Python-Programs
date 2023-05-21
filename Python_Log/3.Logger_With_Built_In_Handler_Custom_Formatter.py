# Logger with built in handler and custom formatter
# the handler object can use a custom formatter object and the handler object 
# can be added to the logger object as its handler before we start using the logger for any log events.

import logging

logger = logging.getLogger("user")
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.critical("This is CRITICAL")
logger.debug("This is DEBUG")
logger.error("This is ERROR")
logger.info("This is INFO")
logger.warning("This is WARNING")
