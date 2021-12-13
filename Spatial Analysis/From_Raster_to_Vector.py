# -*- coding: utf-8 -*-
__author__ = 'voirin'

# on importe les libs
from osgeo import gdal, ogr, osr

gdal.UseExceptions()

# le fichier Raster en vectoriser
fileName = r"../data/alberta_2011_clip.tiff"
# on ouvre le fichier
src_ds = gdal.Open(fileName)
# on récupère la bande #1
srcband = src_ds.GetRasterBand(1)
# on récupère la projection
wkt = src_ds.GetProjection()
# on va définir le fichier vectoriel
dst_layername = "poly_alberta"
# on fait un shapefile
drv = ogr.GetDriverByName("ESRI Shapefile")
# on va créer le fichier
dst_ds = drv.CreateDataSource('../data/' + dst_layername + ".shp")

# on va créer le SRS pour le fichier vectoriel à partir du SRS de l'image
src = osr.SpatialReference()
src.ImportFromWkt(wkt)

# on peut créer un masque si on ne veut pas tout vectoriser
# on fait une copie du fichier original
maskRaster = gdal.GetDriverByName('MEM').CreateCopy('', src_ds, 0)
maskBand = maskRaster.GetRasterBand(1)
# on récupère la matrice
maskData = maskBand.ReadAsArray()
# on va faire un masque binaire
# pixel à exclure 7 -> on doit les mettre à zéro
maskData[maskData==7] = 0
maskBand.WriteArray(maskData)

dst_layer = dst_ds.CreateLayer(dst_layername, srs = src)
# on va créer un champ avec les infos des pixels
newField = ogr.FieldDefn('pixels', ogr.OFTInteger)
dst_layer.CreateField(newField)
# on appel la fonction polygonize
gdal.Polygonize(srcband, maskBand, dst_layer, 0, [], callback=None )
