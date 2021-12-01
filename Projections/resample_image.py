# -*- coding: utf-8 -*-
__author__ = 'voirin'

# on importe GDAL
import gdal
# on déclare le fichier à rééchantillonner
infn = r'..\data\alberta_2011.tiff'
# fichier rééchantillonné
outfn = r'..\data\alberta_2011_200mx200m.tiff'

# résolution spatiale souhaitée 200m x 200m
xres=200
yres=200
# méthode du plus proche voisin
resample_alg = gdal.GRA_NearestNeighbour
# options de la méthode
options = gdal.WarpOptions(options=['tr'], xRes=xres, yRes=yres, resampleAlg=resample_alg)
# on fait le rééchantillonnage
ds = gdal.Warp(outfn, infn, options=options)
ds = None