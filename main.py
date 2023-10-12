"""
# Project: CrimesDelits
# Creation Date: 2023-10-11
# History:
######################################################################################################################################################
#   DATE            AUTHOR      VERSION     ACTION
#   2023-10-11      LLEG        1.0.0       Creation
"""

import logging

from utils.logging import Logging
from utils.constant import Constant

def main() -> None:
    """main method."""
    # load logging config
    Logging()

    log = logging.getLogger(__name__)

    log.debug('Start')

    # call other modules here

    # TODO: move this to the proper module
    import os
    import urllib.request
    import requests

    # Create data folder
    if not os.path.exists(Constant.DATA_FOLDER):
        os.makedirs(Constant.DATA_FOLDER)

    # download data files
    if not os.path.exists(Constant.DATA_FILE):
        urllib.request.urlretrieve(Constant.DATA_URL, Constant.DATA_FILE)
        log.info('data file downloaded')
    if not os.path.exists(Constant.INSTRUCTIONS_FILE):
        response = requests.get(Constant.INSTRUCTIONS_URL, timeout=10)
        with open(Constant.INSTRUCTIONS_FILE, 'wb') as file:
            file.write(response.content)
            log.info('instructions file downloaded')

    log.debug('End')

# start program
if __name__ == '__main__':
    main()
