import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

pasta_datasets = Path(__file__).parent / "datasets"

pasta_datasets.mkdir(parents=True, exist_ok=True)

LOJAS = [
    {'estado': 'CE', 'cidade': 'Fortaleza', 
     'vendedores': ['Ana Oliveira', 'Matheus Pereira']},
    {'estado': 'PE', 'cidade': 'Recife', 
     'vendedores': ['Carlos Silva', 'Fernanda Costa']},
    {'estado': 'BA', 'cidade': 'Salvador', 
     'vendedores': ['Francisco José', 'Carla Montenegro']},
    {'estado': 'RN', 'cidade': 'Natal', 
     'vendedores': ['João Pedro', 'Clara Neves']},
    {'estado': 'SP', 'cidade': 'São Paulo', 
     'vendedores': ['Maurício Peçanha', 'Floriana Peixoto']},
    
]

PRODUTOS = [
    {"nome": "Smartphone Samsung Galaxy", "id":0, "preco": 2500},
    {"nome": "Smartwatch QCY", "id":1, "preco": 360},
    {"nome": "PlayStation 5", "id":2, "preco": 4000},
    {"nome": "SmartTV OLED 4k TCL", "id":3, "preco": 7500},
    {"nome": "Geladeira Eletrolux", "id":4, "preco": 3999},
]

FORMA_PGTO = ['cartão de crédito', 'boleto', 'pix', 'dinheiro']
GENERO_CLIENTES = ['male', 'female']

compras = []

for _ in range(2000):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja['vendedores'])
    produto = random.choice(PRODUTOS)
    hora_compra = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours=random.randint(-5, 5),
        minutes=random.randint(-30, 30)
    )
    genero_cliente = random.choice(GENERO_CLIENTES)
    nome_cliente = names.get_full_name(genero_cliente)
    forma_pgto = random.choice(FORMA_PGTO)

    compras.append({
        "data": hora_compra,
        "id_compra": 0,
        "loja": loja['cidade'],
        "vendedor": vendedor,
        "produto": produto['nome'],
        "cliente_nome": nome_cliente,
        "cliente_genero": genero_cliente.replace("female", "feminino").replace("male", "masculino"),
        "forma_pagamento": forma_pgto
    })

df_compras = pd.DataFrame(compras).set_index("data").sort_index()
df_compras['id_compra'] = [i for i in range(len(df_compras))]

df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)

#Exportando DAtaframes
df_compras.to_csv(pasta_datasets / "compras.csv", decimal= ",", sep= ";")
df_lojas.to_csv(pasta_datasets / "lojas.csv", decimal= ",", sep= ";")
df_produtos.to_csv(pasta_datasets / "produtos.csv", decimal= ",", sep= ";")

df_compras.to_excel(pasta_datasets / "compras.xlsx")
df_lojas.to_excel(pasta_datasets / "lojas.xlsx")
df_produtos.to_excel(pasta_datasets / "produtos.xlsx")