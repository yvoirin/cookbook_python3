# -*- coding: utf-8 -*-
__author__ = 'voirin'

# on importe les libs
import json

# on lit le fichier JSON
json_data = open(r'../data/countries.geo.json').read()

# on charge le contenu du fichier et on le convertit en un dictionnaire PYTHON
data = json.loads(json_data)

# la structure d'un geojson fait en sorte que sous la clé FEATURES, je vais avoir
# une liste d'entités où chaque entité est définie sous la forme d'un dictionnaire
# On peut retrouver les clés suivantes :

# type, properties, geometry

# je parcours les entités du geojson
for c in data['features']:
    # la variable c contient un dictionnaire (équivalent à l'entité)
    # j'affiche le contenu de la clé properties
    if c['properties']['name'] == 'Canada':
        print(c['properties'])
        print(c['geometry'])