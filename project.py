import pandas as pd
import numpy as np
df = pd.read_csv('liquer_sales_2016-2019.csv')
df = pd.DataFrame(df)
groupped_by_zip = df.groupby('zip_code')
print(groupped_by_zip['county','item_description','bottles_sold','sale_dollars'].aggregate(np.max))
print(df.sum('sale_dollars'))




