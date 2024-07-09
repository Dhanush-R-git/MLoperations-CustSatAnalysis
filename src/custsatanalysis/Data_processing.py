import logging
from abc import ABC, abstractmethod
from typing import Union
from custsatanalysis import logger

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataStrategy(ABC):
    """
    Abstract Class defining strategy for handling data
    """
    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass


class DataPreProcessStrategy(DataStrategy):
    """
    Data preprocessing strategy which preprocesses the data.
    """
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        '''
        preprocess the data
        '''
        try:
            data = data.drop(
                [
                    "order_approved_at",
                    "order_delivered_carrier_date",
                    "order_delivered_customer_date",
                    "order_estimated_delivery_date",
                    "order_purchase_timestamp",
                ], axis= 1
            )
            data = data.assign(
                product_weight_g=data["product_weight_g"].fillna(data["product_weight_g"].median()),
                product_length_cm=data["product_length_cm"].fillna(data["product_length_cm"].median()),
                product_height_cm=data["product_height_cm"].fillna(data["product_height_cm"].median()),
                product_width_cm=data["product_width_cm"].fillna(data["product_width_cm"].median()),
                # write "No review" in review_comment_message column
                review_comment_message=data["review_comment_message"].fillna("No review")
                )

            data = data.select_dtypes(include=[np.number])# select only a numerical data 
            cols_to_drop = ["customer_zip_code_prefix", "order_item_id"]
            data = data.drop(cols_to_drop, axis=1)

            return data
        except Exception as e:
            logging.error(e)
            raise e


class DataDivideStrategy(DataStrategy):
    """
    Data dividing strategy which divides the data into train and test data.
    """
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        try:
            X = data.drop(["review_score"], axis=1)
            y = data["review_score"]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error(e)
            raise e
        

class DataCleaning:
    """
    Data cleaning class which preprocesses the data and divides it into train and test data.
    """
    def __init__(self, data: pd.DataFrame, strategy: DataStrategy) -> None:
        """Initializes the DataCleaning class with a specific strategy."""
        self.data = data
        self.strategy = strategy

    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        """Handle data based on the provided strategy"""

        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logger.error("Error in handling data: {}".format(e))
            raise e
        
'''
if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/Dhanush-R-git/Data-Vault/main/olist_customers_dataset.csv"
    data = pd.read_csv(url)
    data_cleaning = DataCleaning(data, DataPreProcessStrategy())
    data_cleaning.handle_data()
'''

