import pandas as pd

ecom_sales = pd.read_csv('dados/ecom_sales.csv')
ecom_sales2 = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales (R$)')