import plotly.express as px
from utils import df_receita_estado, df_receita_mensal, df_categoria, df_vendedores

grafico_mapa_estado = px.scatter_geo(
    df_receita_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    title='Receita por Estado'
)

grafico_receita_mensal = px.line(
    df_receita_mensal,
    x= 'Mês',
    y= 'Preço',
    markers=True,
    range_y= (0, df_receita_mensal['Preço'].max()),
    color='Ano',
    line_dash= 'Ano',
    title='Receita Mensal'
    
)

grafico_receita_mensal.update_layout(yaxis_title='Receita')

grafico_receita_estado = px.bar(
    df_receita_estado.head(7),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Top receita por Estado'
)

grafico_categoria = px.bar(
    df_categoria.head(7),
    text_auto=True,
    title='Top categorias por receita'
)

grafico_vendedores = px.bar(
    df_vendedores[['sum']].sort_values(by='sum', ascending=False).head(7),
    x = 'sum',
    y = df_vendedores[['sum']].sort_values(by='sum', ascending=False).head(7).index,
    text_auto=True,
    title='Top vendedores por receita'
)
grafico_vendas_vendedores = px.bar(
    df_vendedores[['count']].sort_values(by='count', ascending=False).head(7),
    x = 'count',
    y = df_vendedores[['count']].sort_values(by='count', ascending=False).head(7).index,
    text_auto=True,
    title='Top 7 vendedores por Venda'
)