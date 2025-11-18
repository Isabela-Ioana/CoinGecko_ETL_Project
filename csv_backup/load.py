from extract import extract_crypto_data
from transform import transform_crypto_data
import pandas as pd

df_extracted= extract_crypto_data()
df_transformed= transform_crypto_data(df_extracted)

df_transformed.to_csv("csv_backup/crypto_data.csv",index=False)



