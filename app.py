import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

dados_noticias = pd.read_json('noticias.json')
titulo = st.title('Monitoramento de Notícias sobre IA no Piauí')
tabela = st.dataframe(dados_noticias)
sentimentos = dados_noticias['Sentimento'].value_counts()
figura , eixo_do_grafico = plt.subplots()

eixo_do_grafico.pie(sentimentos, labels=sentimentos.index,
                     autopct='%1.1f%%', startangle=90)
eixo_do_grafico.set_title('Distribuição de Sentimento das Notícias')
# Garante que o círculo seja desenhado corretamente
eixo_do_grafico.axis('equal')

# Exibe o gráfico com Streamlit
st.pyplot(figura)
