import requests
from bs4 import BeautifulSoup

# URL da página
url = 'https://www.scrapethissite.com/pages/simple/'

# Requisição HTTP
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Seleciona os blocos de cada país
countries = soup.select('.col-md-4.country')

# Itera e extrai os dados organizados
for country in countries:
    name = country.find('h3', class_='country-name').get_text(strip=True)
    capital = country.find('span', class_='country-capital').get_text(strip=True)
    population = country.find('span', class_='country-population').get_text(strip=True)
    area = country.find('span', class_='country-area').get_text(strip=True)

    print(f'País: {name}')
    print(f'  Capital: {capital}')
    print(f'  População: {population}')
    print(f'  Área (km²): {area}')
    print('-' * 40)
