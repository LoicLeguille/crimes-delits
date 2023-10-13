"""
# Project: CrimesDelits
# Creation Date: 2023-10-11
# History:
######################################################################################################################################################
#   DATE            AUTHOR      VERSION     ACTION
#   2023-10-11      LLEG        1.0.0       Creation
"""

import logging
import time

import pandas as pd

from utils.logging import Logging
from utils.constant import Constant
from utils.functions import download_data_files

def main() -> None:
    """main method."""
    # load logging config
    Logging()

    log = logging.getLogger(__name__)

    starting_time = time.time()

    log.debug('Start')

    # call other modules here

    # TODO: seperate this function in 3.
    # add flags to choose to downloads those files when running the script.
    download_data_files()

    # TODO: move this elsewhere
    # get every sheet name except for the 1st one
    reader = pd.ExcelFile(Constant.DATA_FILE)
    sheets = [s for s in reader.sheet_names if s != 'Présentation']

    # load every sheets except 1st one and store it into a dictonnary
    dict_df = pd.read_excel(Constant.DATA_FILE, header=[0, 1, 2], sheet_name=sheets)

    # drop first column of every dataframe (duplicate information)
    for _, value in dict_df.items():
        value.drop(value.columns[0], axis=1, inplace=True)

    # access MultiIndex columns
    # IndexSlice has 'Départements', 'Périmètres', 'CSP' arguments
    log.debug(dict_df.get('Services PN 2012').loc[:, pd.IndexSlice[["01"], :, :]])

    log.debug('End')
    log.info('Finished successfully in %.2fs', time.time() - starting_time)

# start program
if __name__ == '__main__':
    main()
