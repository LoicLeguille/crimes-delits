"""
# Project: CrimesDelits
# Creation Date: 2023-10-12
# History:
######################################################################################################################################################
#   DATE            AUTHOR      VERSION     ACTION
#   2023-10-12      LLEG        1.0.0       Creation
"""

import os
import logging

import requests

from utils.constant import Constant

log = logging.getLogger(__name__)

def download_file(url: str | bytes, filepath: str | os.PathLike) -> None:
    """download file locally from an url.

    Args:
        url (str | bytes): url of the file to download
        filepath (str | os.PathLike): path to save the file
    """
    log.debug('Start')
    _create_data_folder()

    if not os.path.exists(filepath):
        response = requests.get(url, timeout=10)
        with open(filepath, 'wb') as file:
            file.write(response.content)
            log.info('%s file downloaded', os.path.basename(filepath))
    else:
        log.info('%s file already exists', os.path.basename(filepath))
    log.debug('End')

def _create_data_folder() -> None:
    """create a data folder if it doesn't already exists."""

    log.debug('Start')
    if not os.path.exists(Constant.DATA_FOLDER):
        os.makedirs(Constant.DATA_FOLDER)
        log.info("successfully created data folder")
    log.debug('End')
