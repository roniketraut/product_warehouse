from data_call import extract_fakeapi
import pandas as pd
from datetime import datetime

def clean_data():
    products_df, users_df, carts_df = extract_fakeapi()

    # dropping the not necessary column __v
    users_df.drop(columns = ["__v"], inplace = True)
    carts_df.drop(columns = ["__v"], inplace = True)

    # renaming the columns as apt to the staging tables in pg 
    products_df.rename(columns = {"rating_rate": "rating"}, inplace = True)
    users_df.rename(columns={"name_firstname": "firstname", "name_lastname": "lastname"})

    # changing the data type of date column in date to datetype
    carts_df["date"] = pd.to_datetime(carts_df["date"], errors="raise")
    carts_df["date"] = carts_df["date"].dt.normalize()

    return products_df, users_df, carts_df
