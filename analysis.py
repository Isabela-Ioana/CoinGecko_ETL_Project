import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

df = pd.read_csv("crypto_data.csv")

#Descriptive statistics - see descriptive_analysis.txt
print(df.describe())

