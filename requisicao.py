import requests  # biblioteca de requisições
import xml.etree.ElementTree as ET  # bibliotaca de processar XML
import re
import pandas as pd
from datetime import datetime
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
    "tecnologia", "sustentabilidade", "agilidade", "crescimento", "valorização",
    "eficiência", "excelência", "inédito", "otimização", "empoderamento",
    "digitalização", "melhoria", "impacto", "potencial", "forte",
    "segurança", "progresso", "referência nacional", "inspirador",
    "solução", "avanços", "investimento", "visibilidade", "oportunidade"
]
palavras_contextuais = ["irregularidades",
                        "denúncia", "crime", "problema", "desafio"]

palavras_negativas = [
    "golpe", "prisão", "suspeito", "matar", "homicídio", "urgente",
    "criminalidade", "irregularidades", "endividamento", "risco",
    "problema", "pressão", "desafio", "conflito", "dependência",
    "fraude", "corrupção", "escândalo", "barreira", "falha",
    "ameaça", "perigo", "retrocesso", "instabilidade", "dificuldade",
    "violência", "crime", "roubo", "assalto", "sequestro",
    "abuso", "exploração", "crise", "polêmica", "insegurança",
    "denúncia", "atraso", "déficit", "queda", "fraudes"
]

# lista onda ficara todas as noticias
todas_as_noticias = []


TAG_RE = re.compile(r'<[^>]+>')

# Função que classifica o texto como Positivo, Negativo ou Neutro
def classificacao_do_texto(texto):
    avaliacao_positiva, avaliacao_negativa = 0, 0
    texto_minusculo = texto.lower()

    for palavra in palavras_positivas:
        if palavra in texto_minusculo:
            avaliacao_positiva += 1
    for palavra in palavras_negativas:
        if palavra in texto_minusculo:
            avaliacao_negativa += 1

    for contextual in palavras_contextuais:
        if contextual in texto_minusculo:
            if any(x in texto_minusculo for x in ["detecção", "combate", "prevenção", "monitoramento", "sistema", "tecnologia"]):
                avaliacao_positiva += 1
            else:
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
        pub_date_str = item.find('pubDate').text
        pub_date = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S GMT')

        # Cria dicionário com os dados da notícia
        noticia_dict = {
            'Titulo': titulo,
            'Link': link,
            'Descricao': descricao_limpa.strip(),
            'Sentimento': sentimento,
            'Data': pub_date.strftime('%Y-%m-%d')
        }
        todas_as_noticias.append(noticia_dict)
        
    # Cria um DataFrame a partir da lista de notícias e salva em JSON
    dataframe = pd.DataFrame(todas_as_noticias)
    dataframe.to_json('noticias.json', orient='records', force_ascii=False)

  