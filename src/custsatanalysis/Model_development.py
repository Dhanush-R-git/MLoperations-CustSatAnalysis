from abc import ABC, abstractmethod
from custsatanalysis import logger
from sklearn.linear_model import LinearRegression

class Model(ABC):
    '''
    Abstract Class defining strategy for all models
    '''
    @abstractmethod
    def train(self, X_train, y_train):
        """
        Trains the model on the given data.

        Args:
            x_train: Training data
            y_train: Target data
        """
        pass
class LinearRegressionModel(Model):
    """
    LinearRegressionModel that implements the Model interface.
    """
    def train(self, x_train, y_train, **kwargs):
        '''
        Trains the model
        Args:
            x_train: Training data
            y_train: Target data
        Returns:
            None
        '''
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(x_train, y_train)
            logger.info("Model Training completed")
            return reg
        except Exception as e:
            logger.error("Error in training the model: {}".format(e))
            raise e
