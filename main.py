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
from utils.functions import download_data_files

def main() -> None:
    """main method."""
    # load logging config
    Logging()

    log = logging.getLogger(__name__)

    log.debug('Start')

    # call other modules here
    download_data_files()

    log.debug('End')

# start program
if __name__ == '__main__':
    main()
