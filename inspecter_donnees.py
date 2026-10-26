import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

df = pd.read_parquet("prices.parquet")
"""print(df.head(5))  


print(df.shape)
print(df.columns)
print(df.isna().sum())


print(df.describe())

print(df.dtypes)

print(df['price'].head(10),"\n")
print(df['price'].map(type).value_counts(),"\n")
print(df['price'].drop_duplicates().head(10),"\n")


print(df['price'].dtype)
print(type(df['price'].iloc[0]))
print(df['price'].iloc[0]*2)

# Affiche les 10 devises les plus fréquentes
print(df["currency"].value_counts().head(10))

# Affiche le prix minimum
print(df["price"].min())

# Affiche le prix maximum
print(df["price"].max())

# Affiche le prix médian
print(df["price"].median())
"""
'''idx_man = df['price'].idxmax()
print(df.loc[idx_man].to_string())'''
devise  = df['currency']
print(len(df.loc[devise=="IRR"]))
