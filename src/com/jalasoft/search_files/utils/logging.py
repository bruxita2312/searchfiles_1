import logging.config

from definition import CONFIG_PATH

logging.config.fileconfig(CONFIG_PATH)

logger= logging.getlogger('SearchFiles')