import streamlit as st
from dataset import df
from utils import convert_csv, mensagem_sucesso

st.title("Dataset de Vendas")
st.set_page_config(page_title="Dataset de Vendas", page_icon=":clipboard:")
with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as Colunas',
        list(df.columns),
        list(df.columns)
    )
st.sidebar.title("Filtro de Vendedores")
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
        'Selecione as Categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
    )
with st.sidebar.expander('Preço'):
    preco = st.slider(
        'Selecione o Intervalo de Preço',
        float(df['Preço'].min()),
        float(df['Preço'].max()),
        (float(df['Preço'].min()), float(df['Preço'].max()))
    )
with st.sidebar.expander('Data da Compra'):
    data_compra = st.date_input(
        'Selecione a Data da Compra',
        value=(df['Data da Compra'].min(), df['Data da Compra'].max())
    )

query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= `Preço` <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''
filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.dataframe(filtro_dados)

st.markdown(f"A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas")

st.markdown("Escreva um nome do arquivo")

coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        '',
        label_visibility='collapsed',
    )
    nome_arquivo += '.csv'
with coluna2:
    st.download_button(
        'Baixar Arquivo',
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso
    )