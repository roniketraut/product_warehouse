import pandas
from sqlalchemy import create_engine
import logging
logging.basicConfig(format = '%(levelname)s: %(message)s', level = logging.DEBUG)
from dotenv import load_dotenv
import os
from light_cleaning import clean_data

def load_to_postgres(df, table_name, db_url):
    """Load a DataFrame into PostgreSQL staging table"""
    engine = create_engine(db_url)
    try:
        df.to_sql(table_name, engine, if_exists = 'append', index = False)
    except Exception as e:
        print(f"Error loading {table_name}: {e}")

load_dotenv()
username = os.getenv("PG_USERNAME")
password = os.getenv("PG_PASSWORD")
database = os.getenv("PG_DATABASE")

db_url = f"postgresql://{username}:{password}@localhost:5432/{database}"

products_df, users_df, carts_df = clean_data()

df_table_pairs = [
    ("stg_products", products_df),
    ("stg_users", users_df),
    ("stg_carts", carts_df)
]


def final_call():
    for table, df in df_table_pairs:
        load_to_postgres(df, table, db_url)

final_call()
            
