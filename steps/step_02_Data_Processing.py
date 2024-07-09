from src.custsatanalysis import logger
import pandas as pd
from zenml import step
from src.custsatanalysis.Data_processing import DataCleaning, DataDivideStrategy, DataPreProcessStrategy
from typing_extensions import Annotated
from typing import Tuple

@step
def clean_data(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],
]:
    '''
    Clean the data and divides it into train & test set

    Args:
        df: Raw data
    Returns:
        X_train: Training data
        X_test: Testing data
        y_train: Training labels
        y_test: Testing labels
    '''
    try:
        process_strategy = DataPreProcessStrategy()
        data_cleaning = DataCleaning(df, process_strategy)
        processed_data = data_cleaning.handle_data()

        divide_stratey = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data, divide_stratey)
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logger.info("Splited data into training and testing sets")
        logger.info(f"The shape of Training data is {X_train.shape}, Testing data is {y_train.shape}, \n Training label is {X_test.shape}, Testing label is {y_test.shape}")
        print(f"The shape of x_train is {X_train.shape}, y_train is {y_train.shape}, x_test is {X_test.shape}, y_test is {y_test.shape}")
        logger.info("~~~~~~~~~~~~~~~ Data processing is completed ~~~~~~~~~~~~~~~")
        return X_train, X_test, y_train, y_test
    
    except Exception as e:
        logger.error("Error in processing the data: {}".format(e))
        raise e
