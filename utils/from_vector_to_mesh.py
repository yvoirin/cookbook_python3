# on importe les libs
import fiona
import shapely.geometry
import shapely.ops
import pyproj
import numpy as np
from scipy.interpolate import griddata
import rasterio
from rasterio.transform import Affine

# on définit une reprojection
crs1 = pyproj.CRS('EPSG:4326')
crs2 = pyproj.CRS('EPSG:32198')

project = pyproj.Transformer.from_crs(crs1, crs2, always_xy=True).transform

# on va conserver les points et les valeurs des observations
allpoints = []
values = []
# nos données sont dans un shapefile
with fiona.open('observations.shp') as src:
    # on récupère les points et les valeurs de chaque entité
    for feature in src:
        # on va définir une géométrie et la reprojeter
        shape = shapely.geometry.shape(feature['geometry'])
        newshape = shapely.ops.transform(project, shape)
        # on ajoute les points et les valeurs
        allpoints.append((newshape.x, newshape.y))
        values.append(feature['properties']['temp'])

    # on va définir une grille (meshgrid)
    # on a besoin de trouver les x et y (surtout les extrêmes)
    all_x = [x[0] for x in allpoints]
    all_y = [x[1] for x in allpoints]
    # on définit notre résolution (taille de la cellule)
    res = 10000 # 10 km
    # voici les x et les y
    x = np.arange(min(all_x), max(all_x), res)
    y = np.arange(min(all_y), max(all_y), res)
    # voici notre grille
    xx, yy = np.meshgrid(x, y)
    # pour interpoler, on utilise griddata
    resuinter = griddata(allpoints, values, (xx, yy), method='linear')

    # on va pouvoir conserver le résultat dans une image
    # on définit la géoréférence
    transform = Affine.translation(xx[0][0] - res/2, yy[0][0]-res/2)*Affine.scale(res, res)
    # voici l'image de sortie
    interp = rasterio.open('temperature.tif', 'w', driver='GTiff', height=resuinter.shape[0],
    width=resuinter.shape[1], count=1, dtype=resuinter.dtype, crs=crs2, transform=transform)
    # on écrit les données
    interp.write(resuinter, 1)
    interp.close()