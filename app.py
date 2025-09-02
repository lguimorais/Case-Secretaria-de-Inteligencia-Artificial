import pandas as pd
import streamlit as st

dados_noticias = pd.read_json('noticias.json')
titulo = st.title('Monitoramento de Notícias sobre IA no Piauí')
tabela = st.dataframe(dados_noticias)