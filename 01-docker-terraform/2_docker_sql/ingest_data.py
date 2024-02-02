#!/usr/bin/env python
# coding: utf-8

import argparse
from io import BytesIO
import logging

import pandas as pd
import requests
from sqlalchemy import create_engine

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table 
    color = params.color 
    period = params.period

    url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{color}_tripdata_{period}.csv.gz"
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info(f"Success in requesting data from {url}")

        content = response.content
        df_iter = pd.read_csv(BytesIO(content),  iterator=True, chunksize=100000, compression="gzip")

        df = next(df_iter)

        df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
        df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])


        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

        df.head(0).to_sql(name=table, con=engine, if_exists="append")

        df.to_sql(name=table, con=engine, if_exists='append')

        logging.info(f"Inserted {len(df)} rows to {table} from first chunk")

        while True: 

            df = next(df_iter)

            df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
            df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
            
            df.to_sql(name=table, con=engine, if_exists='append')

            logging.info(f"Inserted {len(df)} rows to {table} from another chunck")
    
    else:
        logging.error(f"Error requesting data. {response.status_code}: {response.content}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")

    parser.add_argument("--user", required=True, help="Username for postgres")
    parser.add_argument("--password", required=True, help="Password for postgres")
    parser.add_argument("--host", required=True, help="Host for postgres")
    parser.add_argument("--port", required=True, help="Port for postgres")
    parser.add_argument("--db", required=True, help="Database for postgres")
    parser.add_argument("--table", required=True, help="Table for postgres")
    parser.add_argument("--color", required=True, help="Color from tripsdata to ingest")
    parser.add_argument("--period", required=True, help="Period from tripsdata to ingest")

    args = parser.parse_args()

    main(args)