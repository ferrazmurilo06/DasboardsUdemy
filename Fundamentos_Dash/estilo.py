from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1('Testando dash com HTML'),
        html.H2('Testando',
            style= {
                'font-size': '50px',
                'color': 'blue'
            }
        ),
        html.Img(
            src='https://avatars.githubusercontent.com/u/113846713?v=4',
            style= {
                'width': '150px',
                'height': '150px'
            }
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)