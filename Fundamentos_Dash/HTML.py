from dash import Dash, dcc, html
from datetime import datetime

app = Dash(__name__)
app.layout = html.Div([
    html.Img(src='https://avatars.githubusercontent.com/u/113846713?v=4'),
    html.Hr(),
    html.H1('Testando o Dash'),
    html.Span(
        children=[
            f'Hoje é {datetime.now().strftime("%d/%m/%Y")}',
            html.Br(),
            'Desenvolvido por: ', html.B('Murilo A Ferraz'),
            html.Br(),
            html.I('Estudante de Ciências da Computação na Universidade Estadual do Ceará (UECE)'),
        ]
    )
])

if __name__ == '__main__':
    app.run(debug=True)