# In this program we are changing the default logger name i.e. "root" to "user",
# and we are also setting it's default log level.
# Create an instance using getLogger()
# Python interpreter will check whether there is already an instance created for this name. 
# If there is already one created, it will return the same instance. 
# After creating a logger instance, we need to make a call to the root logger (basicConfig()) 
# to provide a handler and formatter to our logger. Without any handler configuration, 
# we will get an internal handler as the last resort, which will only output messages without 
# any formatting and the logging level will be WARNING regardless of the logging level we set for our logger. 

import logging

logger_1 = logging.getLogger("user")
logging.basicConfig()

logger_1.setLevel(logging.INFO)
logger_1.critical("This is CRITICAL")
logger_1.debug("This is DEBUG")
logger_1.error("This is ERROR")
logger_1.info("This is INFO")
logger_1.warning("This is WARNING")