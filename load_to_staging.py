import pandas as pd
import logging
logging.basicConfig(format = '%(levelname)s: %(message)s', level = logging.DEBUG)
from dotenv import load_dotenv
import os
from light_cleaning import clean_data
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

load_dotenv()
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_PYTHON_STAGING_SCHEMA = os.getenv("SNOWFLAKE_PYTHON_STAGING_SCHEMA")

def get_snowflake_connection():
    """Establishes a connection to Snowflake"""
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_PYTHON_STAGING_SCHEMA
        )

        logging.info("Successfully connected to Snowflake")
        return conn
    except Exception as e:
        logging.error(f"Error connecting to Snowflake: {e}")
        raise

def load_df_to_snowflake(df: pd.DataFrame, table_name: str, conn: snowflake.connector.SnowflakeConnection):
    target_table_name = table_name.upper()
    df_copy = df.copy()
    df_copy.columns = [col.upper() for col in df_copy.columns]

    try:
        logging.info(f"Attempting to load data into {SNOWFLAKE_DATABASE}.{SNOWFLAKE_PYTHON_STAGING_SCHEMA}.{target_table_name}")

        success, nchunks, nrows, _ = write_pandas(
            conn=conn,
            df=df_copy,
            table_name=target_table_name,
            database=SNOWFLAKE_DATABASE, 
            schema=SNOWFLAKE_PYTHON_STAGING_SCHEMA,   
            auto_create_table=True,
            overwrite=True,
            quote_identifiers=False,
            use_logical_type=True
        )

        if success:
            logging.info(f"Successfully loaded {nrows} rows into {SNOWFLAKE_DATABASE}.{SNOWFLAKE_PYTHON_STAGING_SCHEMA}.{target_table_name} in {nchunks} chunk(s).")
        else:
            logging.error(f"Failed to load data into {target_table_name}. write_pandas reported failure.")

    except Exception as e:
        logging.error(f"Error loading data into Snowflake table {target_table_name}: {e}")

        raise

def main_etl_to_snowflake_staging():
    """Main function to extrat, clean and load data to Snowflake staging"""
    logging.info("Starting ETL process to load data into Snowflake staging")
    try:
        products_df, users_df, carts_df = clean_data()
        print(f"Products DataFrame shape: {products_df.shape if products_df is not None else 'None'}")
        print(f"Users DataFrame shape: {users_df.shape if users_df is not None else 'None'}")
        print(f"Carts DataFrame shape: {carts_df.shape if carts_df is not None else 'None'}")
        logging.info("Light cleaning successful")
    except Exception as e:
        logging.error(f"Error during data extraction or cleaning: {e}")
        return
    
    df_table_pairs = [("stg_products", products_df), ("stg_users", users_df), ("stg_carts", carts_df)]

    conn = None
    try:
        conn = get_snowflake_connection()

        for table_name, df in df_table_pairs:
            if df is not None and not df.empty:
                load_df_to_snowflake(df, table_name, conn)
            else:
                logging.warning(f"Dataframe for table {table_name} is none or empty. Skipping load")

        logging.info("ETL process to Snowflake staging completed successfully")

    except Exception as e:
        logging.error(f"An Error ooccured: {e}")
    finally:
        if conn:
            conn.close()
            logging.info("Snowflake connection closed")

if __name__ == "__main__":
    if not all([SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ACCOUNT, SNOWFLAKE_WAREHOUSE, SNOWFLAKE_DATABASE, SNOWFLAKE_PYTHON_STAGING_SCHEMA]):
        logging.error("One or more required Snowflake environment variables are not set. Please check your .env file or environment.")
    else:
        main_etl_to_snowflake_staging()

            
