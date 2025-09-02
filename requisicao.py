import requests  # biblioteca de requisições
import xml.etree.ElementTree as ET  # bibliotaca de processar XML
import re
import pandas as pd

# termos q vou utilizar como metodo de pesquissa
termos_de_pesquisa = [
    "Inteligência Artificial Piauí", " SIA Piauí", "IA Piauí"]


# url base usado para pegar os conteudos
base_url = "https://news.google.com/rss/search?q={}&hl=pt-BR&gl=BR&ceid=BR%3Apt-419"
# numero de noticias q serão pesquisadas
Num_noticias = 50
palavras_positivas = [
    "avanço", "inovação", "modernização", "referência", "pioneirismo",
    "oportunidades", "gratuito", "qualificação", "capacitação", "parceria",
    "fortalecimento", "protagonismo", "transformação", "revolução", "inclusão",
    "integração", "proteção", "liderança", "sucesso", "premiação",
    "cooperação", "destaque", "desenvolvimento", "expansão", "educação",
    "tecnologia", "sustentabilidade", "agilidade"
]

palavras_negativas = [
    "golpe", "prisão", "suspeito", "matar", "homicídio", "urgente",
    "criminalidade", "irregularidades", "endividamento", "risco",
    "problema", "pressão", "desafio", "conflito", "dependência"
]
# lista onda ficara todas as noticias
todas_as_noticias = []


TAG_RE = re.compile(r'<[^>]+>')


def classificacao_do_texto(texto):
    avaliacao_positiva, avaliacao_negativa = 0, 0
    texto_minusculo = texto.lower()

    for palavra in palavras_positivas:
        if palavra in texto_minusculo:
            avaliacao_positiva += 1
    for palavra in palavras_negativas:
        if palavra in texto_minusculo:
            avaliacao_negativa += 1

    if avaliacao_positiva > avaliacao_negativa:
        return "Positivo"
    elif avaliacao_positiva < avaliacao_negativa:
        return "Negativo"
    else:
        return "Neutro"


for termo in termos_de_pesquisa:
    termo_formatado = termo.replace(" ", "%20")
    url_completa = base_url.format(termo_formatado)
    response = requests.get(url_completa)
    root = ET.fromstring(response.text)
    itens = root.findall('channel/item')

    if not itens:
        print("⚠ Nenhuma notícia encontrada.")
        continue

    for item in itens[:Num_noticias]:
        titulo = item.find('title').text
        link = item.find('link').text
        descricao_bruta = item.find(
            'description').text.replace("&nbsp;&nbsp;", " - ") or " "
        descricao_limpa = TAG_RE.sub('', descricao_bruta)
        texto_completo = titulo + " " + descricao_limpa
        sentimento = classificacao_do_texto(texto_completo)
        noticia_dict = {
            'Titulo': titulo,
            'Link': link,
            'Descricao': descricao_limpa.strip(),
            'Sentimento': sentimento
        }
        todas_as_noticias.append(noticia_dict)
dataframe = pd.DataFrame(todas_as_noticias)
dataframe.to_json('noticias.json')




       # prints utilizados para verificar quais dados estavam vindo para melhor desempenho do codio
        # print("--- Notícia ---")
        # print(f"Título: {titulo}")
        # # print(f"Link: {link}")
        # print(f"Descrição: {descricao_limpa.strip()}")
        # print("-" * 20)
