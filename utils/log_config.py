# Project: CrimesDelits
# Creation Date: 2023-10-11
# History:
######################################################################################################################################################
#   DATE            AUTHOR      VERSION     ACTION
#   2023-10-11      LLEG        1.0.0       Creation

import os
import json
import logging.config
from utils.constant import Constant


class Logging:
    """logging class."""

    @staticmethod
    def load_logging_config(filename: str | os.PathLike | None = "./conf/logging.json") -> None:
        """load a logging config using dictConfig method.

        Args:
            filename (str | os.PathLike | None, optional): json logging file to load. Defaults to "./conf/logging.json".
        """

        with open(filename, 'r', encoding="utf-8") as file:
            config = json.load(file)
            logging.config.dictConfig(config)

    @staticmethod
    def create_log_folder() -> None:
        """create log folder if it doesn't already exists."""
        if not os.path.exists(Constant.LOG_FOLDER):
            os.makedirs(Constant.LOG_FOLDER)
