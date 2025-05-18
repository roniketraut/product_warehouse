import pandas as pd
import requests
from pandas import json_normalize

def extract_fakeapi():
    """Extracting data from fake apis"""

    def extract_product() -> pd.DataFrame:
        """Extracting the product data from the fakeapi"""
        products = requests.get('https://fakestoreapi.com/products/')
        data = products.json()
        products_df = json_normalize(data, sep = "_")
        return products_df

    def extract_users() -> pd.DataFrame:
        users = requests.get("https://fakestoreapi.com/users").json()
        users_df = json_normalize(users, sep = "_")
        return users_df
    
    def extract_carts() -> pd.DataFrame:
        carts = requests.get("https://fakestoreapi.com/carts").json()
        df = pd.DataFrame(carts)

        # exploding the products column
        df_exploded = df.explode('products').reset_index(drop=True)

        # normalizing the nested dictionary inside the products
        products_df = pd.json_normalize(df_exploded["products"])

        # concating everything to make the final carts_df
        carts_df = pd.concat([df_exploded.drop(columns=['products']), products_df], axis=1)

        return carts_df
    
    products_df = extract_product()
    users_df = extract_users()
    carts_df = extract_carts()
    carts_df.drop(columns = ["__v"], inplace = True)

    print(products_df.columns)
    print(users_df.columns)
    print(carts_df.columns)
    return products_df, users_df, carts_df


extract_fakeapi()