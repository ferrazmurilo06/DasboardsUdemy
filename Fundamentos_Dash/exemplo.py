import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

app = Dash(__name__)

# 1- Criando DataFrame:
df = pd.DataFrame({
    'Frutas': ['Maçã', 'Banana', 'Laranja', 'Uva', 'Pera'],
    'Quantidade': [10, 15, 7, 12, 5],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']
})

# 2- Criando gráfico:

fig =px.bar(
    df,
    x='Frutas',
    y='Quantidade',
    color='Cidade',
    title='Quantidade de Frutas por Cidade',
    barmode='group'
)

# fig.show()

# 3- Criando layout do Dash:

app.layout = html.Div(
    children=[
        html.H1('Hello Dash!'),
        html.Div(
            children=[
                '''
                    Dash: A web application framework for your data.
                '''
            ]
        ),
        dcc.Graph(
            id='example-graph',
            figure= fig
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)