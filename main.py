import pandas as pd
import numpy as np
df = pd.read_csv('liquer_sales_2016-2019.csv')
df = pd.DataFrame(df)
total_sales = df['sale_dollars'].sum()
df1 = df.groupby('store_name')['sale_dollars'].sum().reset_index()
df1['%_total'] = (df1['sale_dollars']/total_sales)*100
print(df1)
df2 = df.groupby('zip_code')['sale_dollars'].max()
print(df2)





