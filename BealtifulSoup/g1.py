import requests
from bs4 import BeautifulSoup

request = requests.get('https://g1.globo.com/')

content = request.content

site = BeautifulSoup(content, 'html.parser')

post = site.find('div', attrs={'class': 'feed-post-body'})

#titulo
tittle = post.find('a', attrs= {'class': 'feed-post-link'})

print(tittle.text)

#subtitulo
subtittle = post.find('div', attrs= {'class': 'bstn-fd-relatedtext'})

print(subtittle.text)