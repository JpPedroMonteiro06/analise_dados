# pip install xlrd streamlit plotly pandas
# Rodar: python -m streamlit run EXEMPLO/arquivo.py
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

PASTA = Path(__file__).parent
ARQUIVO = PASTA / "Tabela 1.1.2.xls"

GRUPOS = ["Total", "14 a 29 anos", "30 a 49 anos", "50 a 59 anos", "60 anos ou mais"]
REGIOES = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]


@st.cache_data
def carregar():
    bruto = pd.read_excel(ARQUIVO, header=None)
    col0 = bruto.columns[0]
    inicio = bruto.index[bruto[col0] == "Brasil"][0]
    fim = bruto.index[bruto[col0] == "Distrito Federal"][0]
    df = bruto.loc[inicio:fim, bruto.columns[:16]].copy()

    colunas = ["local"]
    for g in GRUPOS:
        colunas += [f"{g}|Total", f"{g}|Homem", f"{g}|Mulher"]
    df.columns = colunas
    for c in colunas[1:]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    longo = df.melt(id_vars="local", var_name="grupo_sexo", value_name="horas")
    longo[["grupo_idade", "sexo"]] = longo["grupo_sexo"].str.split("|", expand=True)
    longo["tipo"] = "Estado"
    longo.loc[longo["local"].isin(REGIOES), "tipo"] = "Região"
    longo.loc[longo["local"] == "Brasil", "tipo"] = "Brasil"
    return df, longo.drop(columns="grupo_sexo")


st.set_page_config(page_title="Afazeres domésticos - IBGE", layout="wide")
st.title("Horas semanais em cuidados e afazeres domésticos")
st.caption("Pessoas de 14 anos ou mais ocupadas - IBGE, PNAD Contínua 2022 (Tabela 1.1.2)")

tabela, longo = carregar()

with st.sidebar:
    st.header("Filtros")
    nivel = st.radio("Mostrar", ["Região", "Estado"])
    grupo = st.selectbox("Grupo de idade", GRUPOS)
    sexos = st.multiselect("Sexo", ["Homem", "Mulher"], default=["Homem", "Mulher"])

brasil = tabela.loc[tabela["local"] == "Brasil"].iloc[0]
c1, c2, c3 = st.columns(3)
c1.metric("Brasil - total", f"{brasil[f'{grupo}|Total']:.1f} h")
c2.metric("Homens", f"{brasil[f'{grupo}|Homem']:.1f} h")
c3.metric("Mulheres", f"{brasil[f'{grupo}|Mulher']:.1f} h",
          f"{brasil[f'{grupo}|Mulher'] - brasil[f'{grupo}|Homem']:+.1f} h que os homens")

filtro = longo[(longo["tipo"] == nivel) & (longo["grupo_idade"] == grupo) & (longo["sexo"].isin(sexos))]
fig = px.bar(
    filtro.sort_values("horas", ascending=False),
    x="local", y="horas", color="sexo", barmode="group",
    labels={"local": nivel, "horas": "Horas por semana", "sexo": "Sexo"},
    title=f"{grupo}: horas por {nivel.lower()} e sexo",
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Evolução por grupo de idade - Brasil")
br = longo[(longo["local"] == "Brasil") & (longo["grupo_idade"] != "Total") & (longo["sexo"] != "Total")]
fig2 = px.line(br, x="grupo_idade", y="horas", color="sexo", markers=True,
               labels={"grupo_idade": "Grupo de idade", "horas": "Horas por semana"})
st.plotly_chart(fig2, use_container_width=True)

with st.expander("Ver tabela"):
    st.dataframe(tabela, hide_index=True)
