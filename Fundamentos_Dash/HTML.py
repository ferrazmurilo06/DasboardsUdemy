from dash import Dash, dcc, html

app = Dash(__name__)
app.layout = html.Div([
    html.Img(src='https://images.unsplash.com/photo-1507525428034-b723cf961d3e', style={'width': '100%'}),
])