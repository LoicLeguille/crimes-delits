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
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

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
    # ...
    # ...

    # TODO: seperate this function in 3.
    # add flags to choose to downloads those files when running the script.
    download_data_files()

    # TODO: move all this below code elsewhere, use constants when needed
    # get every sheet name except for the 1st one
    reader = pd.ExcelFile(Constant.DATA_FILE)
    sheets = [s for s in reader.sheet_names if s != 'Présentation']

    # load every sheets except 1st one and store it into a dictonnary
    dict_df = pd.read_excel(Constant.DATA_FILE, header=[0, 1, 2], index_col=0, sheet_name=sheets)

    for _, value in dict_df.items():
        # drop first and second columns (doesn't have data)
        value.drop(value.columns[0:1], axis=1, inplace=True)
        # rename levels of MultiIndex columns
        value.columns.rename(['Départements', 'Périmètres', 'CSP'], level=[0, 1, 2], inplace=True)

    # work with dafaframe of Services PN 2012 xlsx sheet
    current_df = dict_df.get('Services PN 2012')
    columns = current_df.columns

    # flatten MultiIndex to 'Départements' level
    current_df.columns = current_df.columns.get_level_values('Départements')

    # plot a graph of summed data by department
    sns.barplot(current_df.loc[93, :][current_df.loc[93, :] != 0], estimator=sum, errorbar=None)
    plt.xticks(rotation=90)
    plt.show()

    # get back MultiIndex
    current_df.columns = columns



    log.debug('End')
    log.info('Finished successfully in %.2fs', time.time() - starting_time)

# start program
if __name__ == '__main__':
    main()
