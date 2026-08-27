import streamlit as st
import pandas as pd

caminho_arquivo = "datasets/compras.csv"

df_compras = pd.read_csv(caminho_arquivo, sep=';', decimal=',', index_col=0)

colunas = list(df_compras.columns)
colunas_selecionadas = st.sidebar.multiselect("Selecione as colunas:", colunas, colunas)

col1, col2 = st.sidebar.columns(2)
col_filtro = col1.selectbox("Seleciona a coluna:", 
               [c for c in colunas if c not in ['id_compra']])
col_valores = col2.selectbox("Slecione o valor:", 
               list(df_compras[col_filtro].unique()))
st_filtrar = col1.button("Filtrar")
st_limpar = col2.button("Limpar")

if st_filtrar:
    st.dataframe(df_compras.loc[df_compras[col_filtro] == col_valores, colunas_selecionadas])
elif st_limpar:
    st.dataframe(df_compras[colunas_selecionadas])
else:
    st.dataframe(df_compras[colunas_selecionadas])