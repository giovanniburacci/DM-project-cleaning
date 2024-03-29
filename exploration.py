import pandas as pd
import csv

df = pd.read_csv('~/Downloads/vehicles.csv')
print(df.shape[0])
print(df[df['posting_year'].isnull()])
print(df['title_status'].unique())
print(df.isna().sum())

