import pandas as pd

df = pd.read_csv('FOOD-DATA-GROUP1.csv')
print(df.head())
print(df.info())
print(df.describe())