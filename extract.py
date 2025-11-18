import json
import pandas as pd
from datetime import datetime
import requests


#Read the key from the json file
def load_api_key():
    with open("config2.json") as f:      #assures that the file will be closed
        config= json.load(f)
    return config["coingecko_api_key"]


#Extract function
def extract_crypto_data():
    api_key=load_api_key()
    url="https://api.coingecko.com/api/v3/coins/markets"
    headers={
        "x-cg-demo-api-key" : api_key
    }

    params={
        "vs_currency" : "usd",
        "order" : "market_cap_desc",
        "per_page" : 50
    }


    response = requests.get(url,headers=headers,params=params)
    if response.status_code!=200:       #200 is the code for a successful GET
        raise Exception(f"API request failed with code: {response.status_code}")
    
    data= response.json()     #.json transforms in Python Objects -> dictionary
    df= pd.json_normalize(data)   #.json_normalize transforms in a DataFrame
    df["etl_timestamp"]=datetime.now()   #we add a column representing the time when we did the extraction
    return df


if __name__=="__main__":
    df= extract_crypto_data()
    print(df.head())

