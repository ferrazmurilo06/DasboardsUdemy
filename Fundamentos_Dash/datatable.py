from dash import Dash, dcc, html, dash_table
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# print(df)

app.layout = html.Div([
    html.Div(children='DataTable com Dash'),
    dash_table.DataTable(
        data=df.to_dict('records')
    )
])

if __name__ == '__main__':
    app.run(debug=True)