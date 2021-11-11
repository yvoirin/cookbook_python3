# -*- coding: utf-8 -*-
__author__ = 'voirin'

# on importe BeautifulSoup
from bs4 import BeautifulSoup
# on lit le document GeoRss
doc = BeautifulSoup(
    open(r'../data/georss3.xml').read(), 'xml')

# on va alimenter la liste avec les infos du fichier XML
messages = []
# on cherche les noeuds ITEM
for node in doc.findAll('item'):
    # on cherche le noeud TITLE dans les noeuds ITEM
    nodeTitle = node.find('title')
    # on cherche le noeud REATOR dans les noeuds ITEM
    nodeCreator = node.find('dc:creator')
    # on alimente notre liste avec les infos
    messages.append([nodeTitle.text, nodeCreator.text])

# on affiche le résultat
for m in messages:
    print(m)