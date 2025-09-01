import requests  # biblioteca de requisições
import xml.etree.ElementTree as ET  # bibliotaca de processar XML
import re
# termos q vou utilizar como metodo de pesquissa
termos_de_pesquisa = ["Inteligência Artificial Piauí"," SIA Piauí"]

# termos_de_pesquisa = ["Inteligência Artificial Piauí OR SIA Piauí"]

# url base usado para pegar os conteudos
base_url = "https://news.google.com/rss/search?q={}&hl=pt-BR&gl=BR&ceid=BR%3Apt-419"
# numero de noticias q serão pesquisadas
Num_noticias = 15

TAG_RE = re.compile(r'<[^>]+>')


for termo in termos_de_pesquisa:
    termo_formatado = termo.replace(" ", "%20")
    url_completa = base_url.format(termo_formatado)
    response = requests.get(url_completa)
    root = ET.fromstring(response.text)
    itens = root.findall('channel/item')

    # if not itens:
    #     print("⚠ Nenhuma notícia encontrada.")
    #     continue

    for item in itens[:Num_noticias]:
        titulo = item.find('title').text
        link = item.find('link').text
        descricao_bruta = item.find('description').text or " "

        descricao_limpa = TAG_RE.sub('', descricao_bruta)

        print("--- Notícia ---")
        print(f"Título: {titulo}")
        print(f"Link: {link}")
        print(f"Descrição: {descricao_limpa.strip()}")
        print("-" * 20)
