import json
import pandas as pd

with open('dados/vendas.json') as file:
    data = json.load(file)

df = pd.DataFrame(data)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

print(df['Data da Compra'])
