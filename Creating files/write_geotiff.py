# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe GDAL et NUMPY
import numpy, sys
from osgeo import gdal
from osgeo.gdalconst import *
# je déclare tous les drivers
gdal.AllRegister()
# le driver que je veux utiliser GEOTIFF
driver = gdal.GetDriverByName("GTiff")

# taille de mon image
rows = 50
cols = 50
# je déclare mon image
# il faut : la taille, le nombre de bandes et le type de données
image = driver.Create("../data/test.tif", cols, rows, 1, GDT_Int32)

# je cherche la bande 1
band = image.GetRasterBand(1)
# je déclare une matrice numpy de 0
# on pourrait imaginer obtenir cette matrice d'un traitement précédent
data = numpy.zeros((rows,cols), numpy.int16)
# j'écris la matrice dans la bande
band.WriteArray(data, 0, 0)
# je vide la cache
band.FlushCache()
band.SetNoDataValue(-99)
# j'efface ma matrice
del data