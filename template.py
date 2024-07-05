import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="custsatanalysis"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/Data_ingestion.py",
    f"src/{project_name}/Data_processing.py",
    f"src/{project_name}/Model_development.py",
    f"src/{project_name}/Model_evaluation.py",
    f"src/{project_name}/Model_storage/__init__.py",
    "__init__.py",
    "config.yaml",
    "materializer/custom_materializer.py",
    "pipelines/__init__.py",
    "steps/__init__.py",
    "run_deployment.py",
    "run_pipeline.py",
    "streamlit_app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for a file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"The {filename} is already exists")
