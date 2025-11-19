from transform import transform_crypto_data
from extract import extract_crypto_data
from sqlalchemy import create_engine

df_extracted= extract_crypto_data()
df_transformed= transform_crypto_data(df_extracted)


#loading to CSV
df_transformed.to_csv("csv_backup/crypto_data.csv",index=False)

#loading to Sqlite
engine = create_engine("sqlite:///crypto_data.db")
df_transformed.to_sql("crypto_market", con=engine, if_exists="replace",index=False)