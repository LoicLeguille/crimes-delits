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
import pandas as pd

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

def read_xlsx(xlsx_path: str | os.PathLike) -> dict[str, pd.DataFrame]:
    """read excel file and returns dictionary of dataframes corresponding to each excel sheets.

    Args:
        xlsx_path (str | os.PathLike): path of the xlsx file to read 

    Returns:
        dict[str, pd.DataFrame]: dictionary of dataframes
    """
    # get every sheet name except for the 1st one
    reader = pd.ExcelFile(xlsx_path)
    sheets = [s for s in reader.sheet_names if s != 'Présentation']

    # load every sheets except 1st one and store it into a dictonnary
    dict_df = pd.read_excel(Constant.DATA_FILE, header=[0, 1, 2], index_col=0, sheet_name=sheets)

    for value in dict_df.values():
        # drop first and second columns (doesn't have data)
        value.drop(value.columns[0:1], axis=1, inplace=True)
        # rename levels of MultiIndex columns
        value.columns.rename(['Départements', 'Périmètres', 'CSP'], level=[0, 1, 2], inplace=True)

    return dict_df

def _create_data_folder() -> None:
    """create a data folder if it doesn't already exists."""

    log.debug('Start')
    if not os.path.exists(Constant.DATA_FOLDER):
        os.makedirs(Constant.DATA_FOLDER)
        log.info("successfully created data folder")
    log.debug('End')
