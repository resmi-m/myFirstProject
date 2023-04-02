import pandas as pd
import numpy as np
import csv
df = pd.read_csv('liquer_sales_2016-2019.csv')
df = pd.DataFrame(df)
total_sales = df['sale_dollars'].sum()
df1 = df.groupby('store_name').sum().reset_index()
df1['%_total'] = (df1['sale_dollars']/total_sales)*100
print(df1)
df2 = df.groupby('zip_code').sum()
print(df2)
df1.to_csv('df1', encoding='utf-8', index=False)
df2.to_csv('df2', encoding='utf-8', index=False)







