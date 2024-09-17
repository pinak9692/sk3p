from src.sk3p.logger import logging #A1
from src.sk3p.exception import CustomException #A2
from src.sk3p.components.data_ingestion import DataIngestion
from src.sk3p.components.data_ingestion import DataIngestionConfig
import sys #A2

#A1
if __name__=="__main__":
    logging.info("The execution has started")#A1

    try:#A2
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

       
        
    except Exception as e:#A2
        logging.info("Custom Exception")
        raise CustomException(e,sys)#A2

