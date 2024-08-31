import requests
from bs4 import BeautifulSoup

url_base = "https://lista.mercadolivre.com.br/"

produto_nome = input("Qual produto você deseja?")

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs= {'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in produtos:
    titulo = produto.find('h2', attrs= {'class': 'ui-search-item__title'})
    print('Título:',titulo.text)

    moeda = produto.find('span', attrs='andes-money-amount__currency-symbol')
    print('moeda:', moeda.text)

    preco = produto.find('span', attrs='andes-money-amount__fraction')
    print('preço:', preco.text)

    link = produto.find('a', attrs= {'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
    print('link:', link['href'])

    print('\n\n')



