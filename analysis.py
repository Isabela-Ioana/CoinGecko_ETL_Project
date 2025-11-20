import pandas as pd 

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

df = pd.read_csv("csv_backup/crypto_data.csv")

#Descriptive statistics - see descriptive_analysis.txt
print(df.describe())



