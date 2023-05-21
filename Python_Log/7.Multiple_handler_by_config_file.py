# The configuration file for a logger can be written using JSON (JavaScript Object Notation) 
# or YAML (Yet Another Markup Language) or as a list of key:value pairs in a .conf file.

import logging
import logging.config
import yaml

with open("logging_by_configuration.conf.yaml", "r") as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("user")

logger.warning("This is WARNING")
logger.error("This is ERROR")
logger.info("This is INFO")
logger.debug("This is DEBUG")