"""
Module: logger
"""

import logging.config
from definition import CONFIG_PATH

logging.config.fileConfig(CONFIG_PATH)

# create logger
logger = logging.getLogger('SearchFiles')


