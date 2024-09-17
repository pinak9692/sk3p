#U1 starts here
import os
import sys
from src.sk3p.exception import CustomException
from src.sk3p.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
#U1 ends here
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


#import pickle
import numpy as np
#U1 starts here
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df
    
    except Exception as ex:
        raise CustomException(ex)