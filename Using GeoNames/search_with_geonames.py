# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe requests
# pour geonames, il faut créer un compte gratuit
import requests
import json
# compte geonames
username = 'xxxxxx'
# terme recherché
term = 'london'

# on définit l'URL
url = 'http://api.geonames.org/search?q=%s&maxRows=10&type=json&username=%s' % (term, username)

params = {}
# je fais la requête
req = requests.get(url= url, params=params)
# on lit le document
data = json.loads(req.text)
# on récupère le dictionnaire d'informations
# on lit les résultats retournés par GeoNames
for d in data['geonames']:
    # on affiche la réponse
    print("Le terme %s peut être %s" % (term, d['fcodeName']))
