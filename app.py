import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

dados_noticias = pd.read_json('noticias.json')
titulo = st.title('Monitoramento de Notícias sobre IA no Piauí')

# Mostra a tabela de notícias interativa no Streamlit
tabela = st.dataframe(dados_noticias)

# Conta quantas notícias possuem cada tipo de sentimento (Positivo, Negativo, Neutro)
sentimentos = dados_noticias['Sentimento'].value_counts()

# Cria uma figura e um eixo para desenhar o gráfico
figura, eixo_do_grafico = plt.subplots()

# Desenha um gráfico de pizza com a distribuição dos sentimentos
# labels=sentimentos.index -> usa os nomes dos sentimentos como rótulos
# autopct='%1.1f%%' -> mostra a porcentagem de cada fatia com uma casa decimal
# startangle=90 -> inicia o gráfico de pizza a partir do ângulo de 90 graus
eixo_do_grafico.pie(sentimentos, labels=sentimentos.index,
                    autopct='%1.1f%%', startangle=90)
eixo_do_grafico.set_title('Distribuição de Sentimento das Notícias')
# Garante que o círculo seja desenhado corretamente
eixo_do_grafico.axis('equal')

# Exibe o gráfico com Streamlit
st.pyplot(figura)
