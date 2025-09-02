import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import requisicao 

if st.button('Coletar ou Atualizar Dados'):
    requisicao.funcao_principal()
dados_noticias = pd.read_json('noticias.json')
titulo = st.title('Monitoramento de Notícias sobre IA no Piauí')

if 'Data' in dados_noticias.columns:
    dados_noticias['Data'] = pd.to_datetime(dados_noticias['Data'])

    # Adiciona filtros de data na barra lateral
    st.sidebar.title('Filtros')
    data_inicio = st.sidebar.date_input(
        'Data de Início', dados_noticias['Data'].min())
    data_fim = st.sidebar.date_input(
        'Data de Fim', dados_noticias['Data'].max())

    # Filtra o DataFrame com base no período selecionado
    dados_filtrados = dados_noticias[
        (dados_noticias['Data'].dt.date >= data_inicio) &
        (dados_noticias['Data'].dt.date <= data_fim)
    ]
else:
    # Se a coluna 'Data' não existir, usa o DataFrame completo
    dados_filtrados = dados_noticias
    st.warning(
        "A coluna 'Data' não foi encontrada. O filtro por data não está disponível.")

# Mostra a tabela de notícias interativa no Streamlit
tabela = st.dataframe(dados_filtrados)

# Conta quantas notícias possuem cada tipo de sentimento (Positivo, Negativo, Neutro)
sentimentos = dados_filtrados['Sentimento'].value_counts()

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

st.markdown("---")
st.markdown("""
_Aviso:_ Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos. O resultado da análise pode ter vieses e limitações.
""")
