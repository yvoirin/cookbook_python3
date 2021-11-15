# -*- coding: utf-8 -*-
__author__ = 'voirin'

# import de la lib OGR
import ogr

import sys
# je définis une connexion
conn=ogr.Open("PG: host='localhost' dbname='my_db' user='my_user' password='my_pwd'")
# je teste si la connexion fonctionne
if conn is None:
    print('Could not open a database or GDAL is not correctly installed!')
    sys.exit(1)
# j'effectue une requête pour obtenir une couche
# il suffit d'une table avec une colonne spatiale
layer = conn.ExecuteSQL("SELECT * FROM MY_TABLE")
# je compte le nombre d'entités
print("Nombre d'entités : %d" % (layer.GetFeatureCount()))
