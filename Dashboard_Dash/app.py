import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

#Carregando dataset

url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
dados = pd.read_csv(url)

histograma = px.histogram(dados, x="Age", title="Distribuição de Idade")

dados['Survived'] = dados["Survived"].astype(str)

boxplot = px.box(dados, x="Survived", y="Age", color="Survived", title="Boxplot de Idades")

boxplot.update_layout(
    legend_title_text="Sobrevivência",
    legend=dict(
        itemsizing="constant",
        title_font=dict(size=14)
    )
    
)

boxplot.add_annotation(
    text="0 - não sobreviveu<br>1 - Sobreviveu",
    xref="paper", yref="paper",
    x=0.5, y=1.1,
    showarrow=False,
    font=dict(size=12),
    align='center'
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Análise do Dataset Titanic"),
    html.Div([
        html.H2("Histograma de Idades"),
        dcc.Graph(figure=histograma)
    ]),
    html.Div([
        html.H2("Boxplot de Idades"),
        dcc.Graph(figure=boxplot)
    ])
])

app.run(debug=True)