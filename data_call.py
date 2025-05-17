import pandas as pd
import requests
from pandas import json_normalize

response = requests.get('https://fakestoreapi.com/products/')
data = response.json()
df = json_normalize(data, sep = "_")
print(df.head())