import logging
from zenml import step
import pandas as pd

@step
def evaluate_model(df: pd.DataFrame) -> None:
    '''
    Evaluation of the model on the ingested data
    Args:
        df: ingested data
    '''
    pass

