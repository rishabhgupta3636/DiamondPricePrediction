import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from src.logger import logging 
from src.exception import customexception
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


## Initialize data injestion configuration class 

@dataclass
class DataIngestionconfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')

## Create DataIngestion class

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion function starts")

        try:
            df = pd.read_csv(os.path.join('notebooks/data','gemstone.csv')) 
            logging.info("Dataset has been read as csv to pd")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train Test Split starts")

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion completed")

            return (
                self.ingestion_config.train_data_path,self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("Error occurred in Data Ingestion")
