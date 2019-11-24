import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re

rURL = 'https://www.atsenergo.ru/js-data'
DATA = 'results/market/calcfacthour'
ID = '102019'
gp = []

r = requests.post(rURL, data={'data': DATA, 'id': ID})
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('div', 'xml-data-row-links')
for link in links:
    gp.append([re.search(r'_(\d+)_', link.find('a').get('href')).group(1), link.find_parent('div').div.text])

pprint(gp)