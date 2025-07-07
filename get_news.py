# Importa o módulo 'requests' para fazer requisições HTTP
import requests

# Importa a biblioteca BeautifulSoup para fazer o parsing (análise) do HTML
from bs4 import BeautifulSoup

# Define a URL do site que será acessado
globo_url = 'https://www.globo.com/'

# Envia uma requisição HTTP GET para a URL especificada e armazena a resposta na variável 'page'
# Isso busca o conteúdo da página HTML como se fosse um navegador acessando o site
page = requests.get(globo_url)

# Obtém o conteúdo HTML da resposta (em formato de texto) e armazena na variável 'resposta'
resposta = page.text

# Cria um objeto BeautifulSoup que interpreta o conteúdo HTML da variável 'resposta'
# O segundo argumento 'html.parser' define qual mecanismo de parsing será usado (padrão do Python)
soup = BeautifulSoup(resposta, 'html.parser')

# Procura por todas as tags <h2> com a classe 'post__title' dentro da estrutura HTML
# Essa busca retorna uma lista com todos os elementos que atendem a esse critério
# (No caso, os títulos de notícias)
noticias = soup.find_all('h2', {'class': 'post__title'})

# Percorre a lista de notícias encontrada
for i in range(len(noticias)):
    # Para cada elemento <h2>, extrai apenas o título da notícia
    # O método .text remove as tags HTML e retorna só o conteúdo textual
    print(noticias[i].text)
