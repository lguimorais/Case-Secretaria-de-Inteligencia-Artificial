# Monitoramento de Notícias sobre Inteligência Artificial no Piauí

Este projeto é uma ferramenta de monitoramento de notícias em tempo real sobre Inteligência Artificial (IA) no estado do Piauí. Ele coleta manchetes do Google Notícias e as classifica automaticamente por sentimento (Positivo, Negativo ou Neutro), fornecendo uma visão geral da percepção pública sobre o tema na região.

## Funcionalidades

- Coleta de Dados: Busca as notícias mais recentes usando a API RSS do Google Notícias com base em termos de pesquisa predefinidos.
- Análise de Sentimento: Classifica cada notícia como "Positiva", "Negativa" ou "Neutra" utilizando um dicionário de palavras-chave.
- Visualização Interativa: Apresenta os dados coletados em uma tabela e em um gráfico de pizza para fácil visualização da distribuição de sentimentos.
- Exportação: Salva os dados processados em um arquivo noticias.json.

## Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Python instalado. O projeto utiliza as seguintes bibliotecas, que podem ser instaladas via pip:

```bash
pip install -r requirements.txt
```
Execução
Executar o Script de Coleta de Dados: O arquivo app.py ao executar clicar no botao (Coletar ou Atualizar Dados) ele é por coletar, processar e salvar as notícias quanto mais vezes clicar mais noticias sao coletadas e acrescentadas ao Json. para cada termo_de_pesquisa sao coletadas 15 noticias em que aparece aquele termo entao por vez sao coletadas 45 noticias:

```Bash
streamlit run app.py
```



Isso criará o arquivo noticias.json com os dados mais recentes.para cada termo_de_pesquisa sao coletadas 15 noticias em que aparece aquele termo entao por vez sao coletadas 45 noticias


A aplicação será aberta automaticamente em seu navegador, exibindo a tabela de notícias e o gráfico de sentimentos.
