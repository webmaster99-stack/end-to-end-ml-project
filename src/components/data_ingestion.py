import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestorConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestor:
    def __init__(self):
        self.ingestion_config = DataIngestorConfig()

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion")

        try:
            df = pd.read_csv("notebook\data\StudentsPerformance.csv")
            logging.info("Reading dataset as a dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train-test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.20, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,  index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,  index=False, header=True)

            logging.info("Data ingestion successful")

            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    ingestor = DataIngestor()
    ingestor.initiate_data_ingestion()