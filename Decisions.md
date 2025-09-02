Justificativas Técnicas e Metodologia

Este projeto foi desenvolvido para atender à necessidade de analisar a percepção pública sobre a Inteligência Artificial no Piauí. As escolhas de arquitetura e tecnologia foram feitas para garantir simplicidade, eficiência e um processo de desenvolvimento e aprendizado contínuo.

Escolhas Tecnológicas

    Coleta de Dados (Python): A escolha do Python com a biblioteca requests foi natural para a tarefa de web scraping (coleta de dados da web). O Python é versátil e possui um ecossistema robusto para essa finalidade. O uso do xml.etree.ElementTree para processar o XML da API RSS do Google Notícias simplificou a extração dos dados necessários (título, link e descrição) de forma nativa e eficiente, sem a necessidade de bibliotecas externas mais complexas como o BeautifulSoup.

    Análise de Sentimento (Classificação Baseada em Dicionário): Em vez de usar modelos de aprendizado de máquina mais complexos, optei por uma abordagem mais direta e controlável. A classificação por dicionário de palavras-chave (Positivas e Negativas) é ideal para este projeto, pois oferece transparência e permite ajustar facilmente a lógica de classificação, garantindo que o resultado seja diretamente influenciado pelos termos que eu defini como relevantes para o contexto da IA no Piauí. Esta abordagem é mais do que suficiente para o objetivo do projeto e tem um baixo custo computacional.

    Armazenamento de Dados (noticias.json): Salvar os dados em formato JSON é uma escolha prática. O formato é legível por humanos e facilmente interoperável, podendo ser consumido por diversas outras aplicações, incluindo a aplicação Streamlit. A biblioteca pandas foi usada para estruturar os dados de forma tabular antes da exportação, facilitando o manuseio e a transformação das notícias em um formato padronizado.

    Visualização (Streamlit e Matplotlib): O Streamlit foi a escolha ideal para criar a interface de usuário de forma rápida e com pouco código. Ele permite transformar o script Python em uma aplicação web interativa em minutos. A combinação com o Matplotlib oferece uma forma simples e eficaz de gerar um gráfico de pizza para visualizar a distribuição de sentimentos de maneira clara e intuitiva, complementando a tabela de notícias.

Metodologia de Desenvolvimento e Aprendizado

O projeto foi construído com o auxílio do Gemini em um processo de aprendizado guiado. As interações com o modelo foram focadas na compreensão da lógica e na sintaxe das bibliotecas, e não em uma simples cópia e cola.

    Compreensão da Lógica: Inicialmente, utilizei o Gemini para explorar as possibilidades de coleta de dados de notícias e as opções para análise de sentimentos. A partir das sugestões e explicações, a lógica do projeto foi estruturada, com a decisão de usar a API RSS e uma abordagem de classificação de sentimentos baseada em dicionário.

    Análise e Adaptação do Código: O código gerado foi analisado e modificado para se adequar exatamente às necessidades do projeto. Isso incluiu a adaptação das funções de coleta e classificação, a definição dos termos de pesquisa e das listas de palavras-chave, e a integração entre os scripts requisicao.py e app.py. A documentação das bibliotecas (requests, pandas, streamlit, matplotlib) foi consultada ativamente para garantir a sintaxe correta e o uso adequado de cada função.

Esse método permitiu que a ferramenta fosse construída com base em um sólido entendimento de cada parte do código, garantindo que eu não apenas obtivesse um resultado funcional, mas também adquirisse conhecimento prático sobre cada etapa do processo de desenvolvimento.