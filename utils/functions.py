"""
# Project: CrimesDelits
# Creation Date: 2023-10-12
# History:
######################################################################################################################################################
#   DATE            AUTHOR      VERSION     ACTION
#   2023-10-12      LLEG        1.0.0       Creation
"""

import os
import urllib.request
import logging

import requests

from utils.constant import Constant

def download_data_files() -> None:
    """download xlsx and pdf files provided on nextcloud."""

    log = logging.getLogger(__name__)
    log.debug('Start')
    # Create data folder
    if not os.path.exists(Constant.DATA_FOLDER):
        os.makedirs(Constant.DATA_FOLDER)

    # download xlsx file
    if not os.path.exists(Constant.DATA_FILE):
        urllib.request.urlretrieve(Constant.DATA_URL, Constant.DATA_FILE)
        log.info('data file downloaded')
    # download pdf file
    if not os.path.exists(Constant.INSTRUCTIONS_FILE):
        response = requests.get(Constant.INSTRUCTIONS_URL, timeout=10)
        with open(Constant.INSTRUCTIONS_FILE, 'wb') as file:
            file.write(response.content)
            log.info('instructions file downloaded')
    log.debug('End')