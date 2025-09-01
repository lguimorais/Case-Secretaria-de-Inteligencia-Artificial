import requests #biblioteca de requisições
import xml.etree.ElementTree as ET #bibliotaca de processar XML
import re

#termos q vou utilizar como metodo de pesquissa
termos_de_pesquisa = ["Iteligência Artificial Piaui", "Governo do estado do piaui","rafael fonteles e inteligencia artificial"]

#url base usado para pegar os conteudos
base_url = "https://news.google.com/rss/search?q={}"

#numero de noticias q serão pesquisadas
Num_noticias = 15

TAG_RE = re.compile(r'<[^>]+>')

for termo in termos_de_pesquisa:
  termo_formatado = termo.replace(" ","%20")
  url_completa = base_url.format(termo_formatado)
  
  response = requests.get(url_completa)
  
  root = ET.fromstring(response.text)
  itens = root.findall('channel/item')[:Num_noticias]



for item in itens:
  titulo = item.find('title').text
  link = item.find('link').text
  descricao_bruta = item.find('description').text
  descricao_limpa = TAG_RE.sub('',descricao_bruta)
  print("--- Notícia ---")
  print(f"Título: {titulo}")
  print(f"Link: {link}")
  print(f"Descrição: {descricao_limpa.strip()}")
  print("-" * 20)
