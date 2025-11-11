import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles.csv')

st.header('Dashboard de Vendas de Carros')

st.write('Vamos explorar os dados de carros!')

# Adicione este botão:
hist_button = st.button('Criar histograma')

# O histograma só aparece quando o botão for clicado:
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros...')
    fig = px.histogram(car_data, x="odometer", title="Distribuição da Quilometragem")
    st.plotly_chart(fig)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para explorar a relação entre quilometragem e preço...')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relação entre Quilometragem e Preço")
    st.plotly_chart(fig_scatter)

build_histogram = st.checkbox('Construir um histograma')

if build_histogram:
    st.write('Construindo um histograma para a coluna odometer')
    fig_check = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_check)