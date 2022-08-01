from bs4 import BeautifulSoup
from lxml import html
import requests
import pymongo
import datetime


request= requests.get('https://www.canalrural.com.br/cotacao/cana/')

soup=BeautifulSoup(request.content, 'html.parser')

data = soup.select('div.sub-title span b')
nome = soup.select('div.table-container div.sub-title h3.title-table')
titulo = soup.select('thead tr th')
dados = soup.select('div tbody tr sorting')


for i in titulo:
    titulo = i.text

for x in nome:
    nome = x.text
    print(x)
    print(nome)



#print(i)
"""print(nome)       
print(dados) 
print(data)
"""
