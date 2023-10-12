"""
# Project: CrimesDelits
# Creation Date: 2023-10-11
# History:
######################################################################################################################################################
#   DATE            AUTHOR      VERSION     ACTION
#   2023-10-11      LLEG        1.0.0       Creation
"""

import os
import json
import logging.config
from utils.constant import Constant


class Logging:
    """classe logging."""

    def __init__(self) -> None:

        if not os.path.exists(Constant.LOG_FOLDER):
            os.makedirs(Constant.LOG_FOLDER)

        logging_config = "./conf/logging.json"

        with open(logging_config, 'r', encoding="utf-8") as file:
            config = json.load(file)
            logging.config.dictConfig(config)
