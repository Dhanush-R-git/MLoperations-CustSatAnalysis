from custsatanalysis import logger

from zenml import step
from sklearn.base import RegressorMixin
from typing_extensions import Annotated
from typing import Tuple

import pandas as pd

from src.custsatanalysis.Model_evaluation import MSE, R2score, RMSE

@step
def evaluate_model(model: RegressorMixin,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Tuple[
    Annotated[float, "mse"],
    Annotated[float, "r2_score"], 
    Annotated[float, "rmse"]
]:
    
    """
    Args:
        model: RegressorMixin
        X_test: pd.DataFrame
        y_test: pd.Series
    Returns:
        r2_score: float
        rmse: float
    """
    try:
        prediction = model.predict(X_test)

        # Using the MSE class for mean squared error calculation
        mse_class = MSE()
        mse = mse_class.Calculate_scores(y_test, prediction)
        
        # Using the R2score class for R2 score calculation
        r2_class = R2score()
        r2_score = r2_class.calculate_score(y_test, prediction)

        # Using the RMSE class for root mean squared error calculation
        rmse_class = RMSE()
        rmse = rmse_class.calculate_score(y_test, prediction)

        return mse, r2_score, rmse
    
    except Exception as e:
        logger.error("Error in Evaluation model: {}".format(e))
        raise e
