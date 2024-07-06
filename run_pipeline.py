from pipelines.P1_training import training_pipeline

if __name__ == "__main__":
    # Run the pipeline
    url= "https://raw.githubusercontent.com/Dhanush-R-git/Data-Vault/main/olist_customers_dataset.csv"
    training_pipeline(data_path=url)
