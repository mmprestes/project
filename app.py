import streamlit as st
import pandas as pd

# Textos 

st.header('Meu Dashboard')
st.sidebar.header("Selecione o filtro")

st.markdown("~~Meu titulo~~")
st.caption("Minha legenda")

pessoas = [
    {
        'Nome': 'Marcelo', 'Idade': 49 
    },
    {
        'Nome': 'Ariane', 'Idade': 47
    },
]

st.write("# Pessoa", pessoas)

# exibicao de dados
df =  pd.DataFrame(data=pessoas)

st.bar_chart(df)

