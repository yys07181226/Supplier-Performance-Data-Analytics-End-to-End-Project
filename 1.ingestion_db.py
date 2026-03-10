
# Use this script to save csv files into database with their filename as tablename
import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# ====================== Database configuration ======================
# According to the actual information configuration of MySQL locally:
MYSQL_USER = "root"
MYSQL_PASSWORD = "7261130Yijizu$"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB = "inventory"

engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}",
    pool_pre_ping=True,
    connect_args={"connect_timeout": 10}  # Connection timeout after 10 seconds
)


def ingest_db(df, table_name, engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


def load_raw_data():
    '''this function will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('original_data'):
        if '.csv' in file:
            df = pd.read_csv('original_data/' + file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start) / 60
    logging.info('--------------Ingestion Complete------------')

    logging.info(f'\nTotal Time Taken: {total_time} minutes')

    # Calculate the total time consumption
    total_time = (time.time() - start) / 60
    print(f'\n✅ All CSV files have been imported successfully! Total time taken:{total_time:.2f} minutes')


if __name__ == '__main__':
    load_raw_data()