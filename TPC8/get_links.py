#! /usr/env/bin python3

from bs4 import BeautifulSoup as bs
import requests

import sys

url = sys.argv[1]

conteudo = requests.get(url)
conteudo = conteudo.text

bs = bs(conteudo,'lxml')

links = bs.find_all('a',href=True)


for i,link in enumerate(links):
    print(link['href'])

