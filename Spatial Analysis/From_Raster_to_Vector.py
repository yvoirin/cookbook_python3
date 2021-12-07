# -*- coding: utf-8 -*-
__author__ = 'voirin'

# on importe les libs
from osgeo import gdal, ogr
import sys
import os

gdal.UseExceptions()

# le fichier Raster en vectoriser
fileName = r"../data/alberta_2011_clip.tiff"
# on ouvre le fichier
src_ds = gdal.Open(fileName)
# on récupère la bande #1
srcband = src_ds.GetRasterBand(1)

# on va définir le fichier vectoriel
dst_layername = "poly_alberta"
# on fait un shapefile
drv = ogr.GetDriverByName("ESRI Shapefile")
# on va créer le fichier
dst_ds = drv.CreateDataSource('../data/' + dst_layername + ".shp")
dst_layer = dst_ds.CreateLayer(dst_layername, srs = None)
# on va créer un champ avec les infos des pixels
newField = ogr.FieldDefn('pixels', ogr.OFTInteger)
dst_layer.CreateField(newField)
# on appel la fonction polygonize
gdal.Polygonize(srcband, None, dst_layer, 0, [], callback=None )
