import os
import sys
from logger import logging
from exception import CustomException
import pandas as pd

from components.data_ingestion_component import DataIngestion
from components.data_transformation_component import DataTransformation
from components.model_trainer_component import ModelTrainer
from components.model_evaluation_component import ModelEvaluation


obj=DataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

model_eval_obj = ModelEvaluation()
model_eval_obj.initiate_model_evaluation(train_arr,test_arr)