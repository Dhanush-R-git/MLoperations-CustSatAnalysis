from abc import ABC, abstractmethod

from custsatanalysis import logger
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class Evaluation(ABC):
    """
    Abstract Class defining the strategy for evaluating model performance
    """
    @abstractmethod
    def Calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        '''
        Calcutates the scores for the model
        Args:
            y_true: True labels
            y_pred: predicted labels
        Returns:
            None
        '''
        pass

class MSE(Evaluation):
    '''
    Evaluation strategy that uses Mean Squared Error
    '''
    def Calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        '''
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            mse: float
        '''
        try:
            logger.info("Calculating Mean Squared Error[MSE].......")
            mse = mean_squared_error(y_true, y_pred)
            logger.info("MSE: {}".format(mse))
            return mse
        except Exception as e:
            logger.error("Error in the calculating MSE: {}".format(e))
            raise e

class R2score(Evaluation):
    '''
    Evaluation strategy that uses r2_score
    '''
    def Calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        '''
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            r2_score: float
        '''
        try:
            logger.info("Calculating r2_score.......")
            r2score = r2_score(y_true, y_pred)
            logger.info("R2 Score: {}".format(r2score))
            return r2score
        except Exception as e:
            logger.error("Error in the calculating R2 Score: {}".format(e))
            raise e
        
class RMSE(Evaluation):
    '''
    Evaluation strategy that uses Root Mean Squared Error (RMSE)
    '''
    def Calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        """
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            rmse: float
        """
        try:
            logger.info("Calculating Root Mean Squared Error[RMSE]........")
            rmse = np.sqrt(mean_squared_error(y_true, y_pred))
            logger.info("RMSE: {}".format(rmse))
            return rmse
        except Exception as e:
            logger.error("Error in the calculating RMSE: {}".format(e))
            raise e
