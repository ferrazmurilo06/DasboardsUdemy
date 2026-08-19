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