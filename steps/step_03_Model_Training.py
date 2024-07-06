import logging
import pandas as pd

from zenml import step


@step
def train_model(df: pd.DataFrame) -> None:
    '''
    trains the model from ingested data

    Args:
        df: the ingested data
    '''
    pass