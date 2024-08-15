import numpy as np
import pandas as pd
import seaborn as sns

df=sns.load_dataset("titanic")
df1=sns.load_dataset("titanic")

df["age2"]=df["age"]*2
df["age3"]=df["age"]*5


#Apply kullanimi
print(df.loc[:,df.columns.str.contains("age")].apply(lambda x:x/10).head())

#Concat kullanimi

print(pd.concat([df,df1],ignore_index=True))

#Merge Kullanimi

print(pd.merge(df,df1))

