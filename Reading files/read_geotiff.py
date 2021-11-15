# -*- coding: utf-8 -*-
__author__ = 'voirin'

# import gdal
import gdal, sys
from gdalconst import *
gdal.AllRegister()

# fichier à lire
filename = r"../data/alberta_2011.tiff"
# on ouvre le fichier
ds = gdal.Open(filename, GA_ReadOnly)

if ds is None:
 print('Could not open ' + filename)
 sys.exit(1)
# on lit le nombre de lignes, colonnes, bandes
cols = ds.RasterXSize
rows = ds.RasterYSize
bands = ds.RasterCount
print(cols, rows, bands)

# récupération de la géoréférence de l'image
geotransform = ds.GetGeoTransform()
originX = geotransform[0]
originY = geotransform[3]
pixelWidth = geotransform[1]
pixelHeight = geotransform[5]
# on a un tuple avec 6 valeurs
print(geotransform)

# récupération de la matrice de la bande 1
band = ds.GetRasterBand(1)
# data est une matrice numpy
data = band.ReadAsArray(0, 0, cols, rows)
print(data)


