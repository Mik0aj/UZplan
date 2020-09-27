import io
import requests
import asyncio
import aiohttp
import scrap as sc
from bs4 import BeautifulSoup
import pandas as pd
from html.parser import HTMLParser

def get_links(html):
    """Returns only links from passed html"""
    links = set()
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        links.add(link.get('href'))
    return links


class Plan:
	def __init__(self,degree,group):
		self.degree=degree
		self.group=group
		
# uzyskiwanie linków do wszystkich kierunków na UZ
url = 'http://www.plan.uz.zgora.pl/grupy_lista_kierunkow.php'
r = requests.get(url)
links=get_links(r.text)
newlinks=[]
for link in list(links):
	if 'kierunek=' in link:
		link='http://www.plan.uz.zgora.pl/{}'.format(link)
		newlinks.append(link)
		print(link)
links=newlinks
#dfs = pd.read_html('http://www.plan.uz.zgora.pl/grupy_plan.php?pId_Obiekt=22649',header=0)
#df=dfs[0]
#values=['Poniedziałek','Wtorek','Środa','Czwartek','Piątek','B']
#print(df[df.PG.isin(values)])


