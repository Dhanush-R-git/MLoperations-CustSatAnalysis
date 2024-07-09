from custsatanalysis import logger
import pandas as pd

from zenml import step
from src.custsatanalysis.Model_development import LinearRegressionModel
from sklearn.base import RegressorMixin
from .config import ModelNameConfig

@step
def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    config: ModelNameConfig,
) -> LinearRegressionModel:
    '''
    trains the model from ingested data

    Args:
        X_train: pd.DataFrame,
        X_test: pd.DataFrame,
        y_train: pd.Series,
        y_test: pd.Series,
    '''
    try:
        '''
        Trains the model Args:
            x_train: Training data
            y_train: Target data
        Returns:
            None
        '''
        model = None
        if config.model_name == "LinearRegression":
            model = LinearRegressionModel()
            trained_model = model.train(X_train, y_train)
            return trained_model
        else:
            raise ValueError("Model {} not supported".format(config.model_name))
    except Exception as e:
        logger.error("Error in training model: {}".format(e))
        raise e
    