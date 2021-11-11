# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe la lib
import ogr
# je déclare le fichier à lire (ajuster le chemin selon votre machine)
filename = r'../data/world.shp'
# je déclare un driver SHP
driver = ogr.GetDriverByName('ESRI Shapefile')
# j'ouvre le fichier
datasource = driver.Open(filename)
# je vais chercher la couche
layer = datasource.GetLayer()
# je vais alimenter cette liste coutries avec les infos du Shapefile
countries = []
# je parcours les entités
for feature in layer:
    # j'ajoute dans ma liste le nom du pays et sa géométrie
    countries.append(
        # on récupère les infos de l'entité
        [feature.GetField('name'), feature.GetGeometryRef().Clone()]
    )

print(len(countries))