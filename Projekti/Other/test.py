import pandas as pd
import numpy as np
from sklearn import preprocessing 
from sklearn.preprocessing import Normalizer
print("Hello world")

df = pd.read_csv('MachineLearning/Projekat I/updated_pollution_dataset.csv')
df.info()
print(df.head())
#print(pd.unique(df['Air Quality']))
#m=df['Temperature'].mean()
#print((df['Air Quality']).dtypes

for col in df.columns:
    if df[col].dtypes!=object:
        print(f"{col} mean:{np.round(df[col].mean(),2)}, median:{df[col].median()}")

print(df['Air Quality'].value_counts().to_dict())
minmax_scale=preprocessing.MinMaxScaler(feature_range=(0,1))
scaller=preprocessing.StandardScaler()
df_minmax=df.copy()
df_std=df.copy()

for col in df.columns:
    if df[col].dtypes!=object:
        df_minmax[col]=minmax_scale.fit_transform(df[col].values.reshape(-1,1))
        df_std[col]=scaller.fit_transform(df[col].values.reshape(-1,1))

print(df_minmax.head())
print(df_std.head())