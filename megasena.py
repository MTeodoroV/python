import requests
from bs4 import BeautifulSoup


req = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/')

soup = BeautifulSoup (req.content, 'html.parser')

tabela = soup.select('table.cot-fisicas thead tbody tr td')

print (soup)
for i in tabela:
    print (i.text)


# soup.select ('table.cot-fisicas )