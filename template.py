import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion_component.py",
    "src/components/data_transformation_component.py",
    "src/components/data_validation_component.py",
    "src/components/model_evaluation_component.py",
    "src/components/model_trainer_component.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/utils/utils.py",
    "src/config/__init__.py",
    "src/logger/logger.py",
    "src/exception/exception.py",
    "src/exception/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/pipeline/step_01_data_ingestion_pipeline.py",
    "src/pipeline/step_02_data_validation_pipeline.py",
    "src/pipeline/step_03_data_transformation_pipeline.py",
    "src/pipeline/step_04_model_trainer_pipeline.py",
    "src/pipeline/step_05_model_evaluation_pipeline.py",
    "src/pipeline/step_06_prediction_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/pipeline/training_pipeline.py",
    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    "src/constants/__init__.py",
    "data/data.txt",
    "config/config.yaml",
    "artifacts/info.txt",
    "test/__init__.py",
    "airflow/dags/batch_prediction.py",
    "airflow/dags/training_pipeline.py",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "start.sh",
    "dvc.yaml",
    "Dockerfile",
    "docker-compose.yaml",
    "tox.ini",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "research/trials.ipynb",
    "templates/index.html",
    "templates/form.html",
    "templates/result.html",
    "pyproject.toml",
    "init_setup.sh",
    ".github/workflows/.gitkeep"


]



for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")