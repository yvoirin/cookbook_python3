# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe OGR
from osgeo import ogr, osr

# Je déclare un système de coordonnées (wgs84)
spatialReference = osr.SpatialReference()
spatialReference.ImportFromEPSG(4326)

# je déclare le chemin du fichier à écrire
path=r'../data/points.shp'
# je déclare le driver que je veux utiliser
driver = ogr.GetDriverByName('ESRI Shapefile')
# je créé un datasource pour mes données
shapeData = driver.CreateDataSource(path)
# je créé une couche de points
layer = shapeData.CreateLayer('customs',spatialReference, ogr.wkbPoint)

# je recherche la définition de la couche(attributs)
layer_defn = layer.GetLayerDefn()
# je définis un attribut (nom et type)
new_field= ogr.FieldDefn('NAME', ogr.OFTString)
# je l'ajoute à la couche
layer.CreateField(new_field)

# afin de réduire le code, je vais déclarer un tableau avec les informations à écrire pour chaque point
points = [
     {'lat': 45.399896, 'lon': -71.884232, 'name': 'Sherbrooke'},
     {'lat': 45.536896, 'lon': -73.510551, 'name': 'Longueuil'}
 ]
cnt = 0
for p in points:
     # je déclare mon objet point
     point = ogr.Geometry(ogr.wkbPoint)
     # voici mon point
     point.AddPoint(p['lon'], p['lat'])
     # voici son index
     featureIndex = cnt
     # je créé l'entité avec la définition des attributs
     feature = ogr.Feature(layer_defn)
     # je lui associe une géométrie
     feature.SetGeometry(point)
     # je définis l'index
     feature.SetFID(featureIndex)
     # je vais ajouter la valeur d'un attribut
     feature.SetField("NAME",p['name'])
     # j'ajoute l'entité a la couche
     layer.CreateFeature(feature)
     cnt += 1

# je termine l'édition
shapeData.Destroy()