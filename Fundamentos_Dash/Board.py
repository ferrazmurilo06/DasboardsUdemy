from plotly_bar import bar_fig
from dash import Dash, dcc, html

app = Dash(__name__)

# app.layout = dcc.Graph(
#     id='example-graph',
#     figure=bar_fig
# )

app.layout = html.Div([
    html.H1('Total Sales by Country'),
    dcc.Graph(
        id='bar-graph',
        figure=bar_fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)