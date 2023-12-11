# Project: CrimesDelits
# Creation Date: 2023-10-11
# History:
######################################################################################################################################################
#   DATE            AUTHOR      VERSION     ACTION
#   2023-10-11      LLEG        1.0.0       Creation

class Constant:
    """constant class."""

    # Constant for data folder path
    DATA_FOLDER = "./data"

    # Constant for log folder path
    LOG_FOLDER = "./logs"

    # Constant for data file path
    DATA_FILE = "./data/crimes-delits.xlsx"

    # Constant for instructions file path
    INSTRUCTIONS_FILE = "./data/instructions.pdf"

    # Constant for documentation file path
    DOCUMENTATION_FILE = "./data/documentation.docx"

    # Constant for geojson file
    GEOJSON_FILE = 'data\contour-des-departements.geojson'

    # Constant for data url
    DATA_URL = "https://cloud.crossdata.tech/s/n6WpQJ9Bpxgtg7D/download/crimes-et-delits-enregistres-par-les-services-de-gendarmerie-et-de-police-depuis-2012.xlsx"

    # Constant for instructions url
    INSTRUCTIONS_URL = "https://cloud.crossdata.tech/s/s7zTSRCn6oSYC4S/download/Mission%202.pdf"

    # Constant for documentation url
    DOCUMENTATION_URL = "https://www.data.gouv.fr/fr/datasets/r/7c7edac3-d598-42df-a58b-1ac2e0a0a392"

    # Constant for geojson url
    GEOJSON_URL = "https://www.data.gouv.fr/fr/datasets/r/90b9341a-e1f7-4d75-a73c-bbc010c7feeb"

    # Constant for choosen index
    CHOSEN_INDEX = [34,35,36]
    #[29, 30]
    # [8,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29, 30,39,40]
    # [29, 30]


    # Constant for the year to split between train and test data
    TRAIN_TEST_SPLIT_YEAR = '2021'

    # Constant service
    SERVICE = 'GN'