import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from src.logger import logging
from src.exception import customexception
from src.components.data_injestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import pandas as pd

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)  

    data_transformation=DataTransformation()

    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)