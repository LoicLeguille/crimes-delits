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

def download_data_files() -> None:
    """download xlsx and pdf files provided on nextcloud."""

    log = logging.getLogger(__name__)
    log.debug('Start')
    # Create data folder
    if not os.path.exists(Constant.DATA_FOLDER):
        os.makedirs(Constant.DATA_FOLDER)

    # download xlsx file
    if not os.path.exists(Constant.DATA_FILE):
        response = requests.get(Constant.DATA_URL, timeout=10)
        with open(Constant.DATA_FILE, 'wb') as file:
            file.write(response.content)
            log.info('data file downloaded')
    else:
        log.info('data file already exists')

    # download pdf file
    if not os.path.exists(Constant.INSTRUCTIONS_FILE):
        response = requests.get(Constant.INSTRUCTIONS_URL, timeout=10)
        with open(Constant.INSTRUCTIONS_FILE, 'wb') as file:
            file.write(response.content)
            log.info('instructions file downloaded')
    else:
        log.info('instructions file already exists')

    # download docx file
    if not os.path.exists(Constant.DOCUMENTATION_FILE):
        response = requests.get(Constant.INSTRUCTIONS_URL, timeout=10)
        with open(Constant.DOCUMENTATION_FILE, 'wb') as file:
            file.write(response.content)
            log.info('documentation file downloaded')
    else:
        log.info('documentation file already exists')

    log.debug('End')
