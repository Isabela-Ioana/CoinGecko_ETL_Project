from transform import transform_crypto_data
from extract import extract_crypto_data
from sqlalchemy import create_engine

df_extracted= extract_crypto_data()
df_transformed= transform_crypto_data(df_extracted)

engine = create_engine("sqlite:///crypto_data.db")
df_transformed.to_sql("crypto_market", con=engine, if_exists="replace",index=False)