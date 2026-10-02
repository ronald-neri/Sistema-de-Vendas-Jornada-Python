# Título Sistema de vendas
# Seção Cadastrar vendas
    # Campo data
    # Campo vendedor - ana, bruno, carla
    # Campo produto - Notebook, Celular, Fone
    # Campo quantidade
    # Campo valor unitário
    # Botão cadastrar venda
        # Quando eu clicar no botão => atualizar a venda na tabela
# Seção Vendas cadastradas
    # Tabela com as vendas cadastradas
# Seção Dashboard
    # Card/Métrica => Faturamento total
    # Gráfico de barra/coluna => Vendas por vendedor
    # Gráfico de pizza => Vendas por produto

# streamlit pandas plotly

import streamlit as st
import pandas as pd
import plotly.express as px

st.write("# Sistema de Vendas")

# carregar vendas cadastradas
tabela_vendas = pd.read_csv("4vendas.csv")

# Seção Cadastrar vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data da venda", min_value=pd.to_datetime("2025-01-01"), max_value=pd.to_datetime("today"))
vendeddor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", min_value=1, step=1)
valor = st.sidebar.number_input("Valor unitário")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# lógica para cadastrar venda
if botao_cadastrar:
    if valor <= 0:
        st.error("O valor unitário deve ser maior que zero.")
    else:
        nova_venda = [str(data), vendeddor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("4vendas.csv", index=False)
        st.success("Venda cadastrada com sucesso!")

# Seção visualização de vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# Seção Dashboard
st.write("## Dashboard")
# Card/Métrica => Faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento:,.2f}")
# Gráfico de barra/coluna => Vendas por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", title="Vendas por vendedor", color="produto")
st.plotly_chart(grafico1)
# Gráfico de pizza => Vendas por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", title="Vendas por produto", hole=0.5)
st.plotly_chart(grafico2)