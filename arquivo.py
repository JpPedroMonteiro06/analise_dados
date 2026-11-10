# Rodar: python -m streamlit run streamlit_aula1/arquivo.py
import pandas as pd
import streamlit as st

itens = [
    "Pão Francês (kg)",
    "Pão de Queijo (un)",
    "Leite Integral (L)",
    "Queijo Mussarela (g)",
    "Presunto (g)",
    "Café Espesso (un)",
    "Bolo de Cenoura (fatia)",
]

# Lista com os respectivos valores em Reais (R$)
precos = [14.90, 2.50, 5.80, 12.50, 9.80, 6.00, 8.50]

vendas = pd.DataFrame({"item": itens, "preco": precos})

st.title("Meu primeiro dash")
st.subheader("Vendas da padaria")

st.write("Tabela de produtos e preços:")
st.dataframe(vendas, hide_index=True)

escolhido = st.selectbox("Escolha um item", vendas["item"])
preco = vendas.loc[vendas["item"] == escolhido, "preco"].item()
st.write(f"O preço de **{escolhido}** é R$ {preco:.2f}".replace(".", ","))
