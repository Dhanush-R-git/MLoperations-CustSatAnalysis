from zenml import pipeline
from steps.step_01_Data_Ingestion import ingest_data
from steps.step_02_Data_Processing import clean_data
from steps.step_03_Model_Training import train_model
from steps.step_04_Model_Evaluation import evaluate_model

@pipeline(enable_cache=True)
def training_pipeline(data_path: str):
    df= ingest_data(data_path)
    clean_data(df)
    train_model(df)
    evaluate_model(df)
