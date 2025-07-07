'''
1. Importa a biblioteca 'requests' para fazer requisições HTTP
2. Importa a biblioteca 'pandas' para manipulação e estruturação de dados em formato tabular
3. Importa o 'BeautifulSoup' da biblioteca 'bs4' para fazer parsing do HTML

'''
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define a função que irá realizar o scraping para uma determinada unidade federativa (UF)
def scraping_uf(uf: str) -> pd.DataFrame:
    # Monta a URL da página do IBGE referente à UF informada
    uf_url = f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html'
    
    # Envia uma requisição HTTP GET para a URL e armazena a resposta
    page = requests.get(uf_url)

    # Cria o objeto BeautifulSoup com o conteúdo da página e define o parser como 'html.parser'
    soup = BeautifulSoup(page.content, 'html.parser')

    # Seleciona todos os elementos HTML com a classe 'indicador' (contêm os dados de interesse)
    indicadores = soup.select('.indicador')

    # Cria um dicionário com os dados dos indicadores
    # A chave será o texto da classe 'ind-label' (nome do indicador)
    # O valor será o texto da classe 'ind-value' (valor do indicador)
    uf_dict = {
        dado.select('.ind-label')[0].text.strip(): dado.select('.ind-value')[0].text.strip()
        for dado in indicadores
    }

    # Limpeza dos dados: remove possíveis caracteres extras nos valores dos indicadores
    for indicador in uf_dict:
        # Se o valor contiver ']', divide no caractere e remove os últimos 8 caracteres da parte anterior
        if ']' in uf_dict[indicador]:
            uf_dict[indicador] = uf_dict[indicador].split(']')[0][:-8]
        else:
            # Caso contrário, mantém o valor como está
            uf_dict[indicador] = uf_dict[indicador]

    # Converte o dicionário em um DataFrame do Pandas, com os indicadores como índice
    # Os valores são colocados na coluna chamada 'Valor'
    df = pd.DataFrame(uf_dict.values(), index=uf_dict.keys(), columns=['Valor'])

    # Retorna o DataFrame gerado
    return df

# Chamada da função com a sigla do Estado desejado 'sp' (São Paulo)
df_rj = scraping_uf('sp')

# Exibe o DataFrame resultante no terminal
print(df_rj)
