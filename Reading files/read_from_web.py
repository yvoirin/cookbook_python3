# -*- coding: utf-8 -*-
__author__ = 'voirin'

# on importe BeautifulSoup
from bs4 import BeautifulSoup
# on import requests
import requests
# on définit l'URL
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom'

params = {}
# je fais la requête
req = requests.get(url= url, params=params)
# on lit le document
doc = BeautifulSoup( req.text, 'xml')

# on va alimenter la liste avec les infos du fichier XML
messages = []
# on cherche les noeuds Entry
for node in doc.findAll('entry'):
    # on cherche le noeud TITLE dans les noeuds ITEM
    nodeTitle = node.find('title')
    # on cherche le noeud REATOR dans les noeuds ITEM
    point = node.find('georss:point')
    # on alimente notre liste avec les infos
    messages.append([nodeTitle.text, point.text])

# on affiche le résultat
for m in messages:
    print(m)
