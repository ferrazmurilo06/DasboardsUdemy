import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_mapa_estado, grafico_receita_mensal, grafico_receita_estado, grafico_categoria, grafico_vendedores, grafico_vendas_vendedores

st.title("Dashboard de Vendas :shopping_cart:")
st.set_page_config(page_title="Dashboard de Vendas", page_icon=":bar_chart:", layout="wide")

aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

with aba1:
    st.dataframe(df)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$ '))
        st.plotly_chart(grafico_mapa_estado, use_container_width=True)
        st.plotly_chart(grafico_receita_estado, use_container_width=True)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_receita_mensal, use_container_width=True)
        st.plotly_chart(grafico_categoria, use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_vendedores)
    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores)