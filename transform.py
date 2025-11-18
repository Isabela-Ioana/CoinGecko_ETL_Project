import pandas as pd
from extract import extract_crypto_data

def transform_crypto_data(df):
    columns_to_keep=[
        "id","symbol","name","current_price","market_cap","total_volume",
        "price_change_24h", "price_change_percentage_24h", "last_updated",
        "etl_timestamp"
    ]
    df=df[columns_to_keep]

    #transformation to numeric and date

                                    # df["current_price"]= pd.to_numeric(df["current_price"],errors="coerce")  #coerce= any non-numeric values transformed in NaN
                                    # df["market_cap"]=pd.to_numeric(df["market_cap"],errors="coerce")
                                    # df["total_volume"]=pd.to_numeric( df["total_volume"],errors="coerce")
                                    # df["price_change_24h"]= pd.to_numeric(df["price_change_24h"],errors="coerce")

    columns_tobenumeric=["current_price","market_cap","total_volume",
       "price_change_24h", "price_change_percentage_24h"]
    for col in columns_tobenumeric:
        df[col]=pd.to_numeric(df[col],errors="coerce")

    columns_tobedate=["last_updated", "etl_timestamp"]
    for col in columns_tobedate:
        df[col]=pd.to_datetime(df[col],errors="coerce")

    columns_tobepositive=["current_price", "market_cap", "total_volume"]
    for col in columns_tobepositive:
        raise ValueError(f"Column {col} has negative value/s!")
    
    if df.duplicated(subset=["id"]).any():
        raise ValueError("Duplicate IDs have been found!")



    df.dropna(subset=["id", "symbol", "current_price"],inplace=True)

    return df

if __name__=="__main__":
    
    df_extracted= extract_crypto_data()

    df_cleaned= transform_crypto_data(df_extracted)
    print(df_cleaned.head())