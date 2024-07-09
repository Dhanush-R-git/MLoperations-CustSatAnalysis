
import pandas as pd

from custsatanalysis import logger
from zenml import step


class DataIngestion:
    """
    Data ingestion class which ingests data from the source and returns a DataFrame.
    """
    def __init__(self, data_path: str):
        '''
        Args:
            data_path: path to the data
        '''
        self.data_path = data_path

    def get_data(self):
        logger.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)
    
@step
def ingest_data(data_path: str) -> pd.DataFrame:
    """
    Ingesting the data from the data path

    Args:
        data_path: path to the data
    returns:
        pd.DataFrame: the ingested data

    """
    try:
        ingest_data = DataIngestion(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logger.error(f"Error while ingesting data: {e}")
        raise e
