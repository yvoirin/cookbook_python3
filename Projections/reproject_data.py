# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe OGR
from osgeo import ogr, osr
# je déclare le chemin vers le fichier
# il faut ajuster en fonction de votre répertoire
shpfile = r'../data/world.shp'
# je déclare un Pilote SHP
driver = ogr.GetDriverByName('ESRI Shapefile')
# # j'ouvre le fichier
datasource = driver.Open(shpfile)
# je cherche les couches
layer = datasource.GetLayer()

feature = layer.GetNextFeature()

# on déclare 2 systèmes de coordonnées (wgs84 et euro lambert)
# on va reprojeter la géométrie 
# système WGS84 (lat/lon)
spatialReferenceSRC = osr.SpatialReference()
spatialReferenceSRC.ImportFromEPSG(4326)
# système Euro lambert (mètre)
spatialReferenceDEST = osr.SpatialReference()
spatialReferenceDEST.ImportFromEPSG(2192)
# fonction permettant de passer d'un système à un autre
transform = osr.CoordinateTransformation(spatialReferenceSRC, spatialReferenceDEST)
while feature:
     if feature.GetField('NAME') == 'FRANCE':
         print(feature.GetField('NAME'))
         print(feature.GetField('APPROX'))
         print(feature.GetField('CAPITAL'))
         geography = feature.GetGeometryRef()
         # on reprojète la géométrie
         geography.Transform(transform)
         # on calcule la superficie en km2
         print("%.2f km2" % (geography.GetArea() / 1000000.0))

     feature = layer.GetNextFeature()