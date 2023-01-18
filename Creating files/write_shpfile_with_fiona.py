# on importe les libs
import fiona
from fiona.crs import from_epsg
from shapely.geometry import Point, mapping
# on imagine un jeu de données à sauvegarder
# nos points sont sous la forme long, lat et nom
data = [
    [-5, -5, 'test'],
    [-1, -3, 'test 1']
]
# on définit le schéma de notre couche
schema = {
    'geometry': 'Point',
    'properties': {'name': 'str'}
}
# on peut maintenant créer notre shapefile
with fiona.open('myshape.shp', 'w', crs=from_epsg(3857),
                driver='ESRI Shapefile', schema=schema) as out:
    # on parcourt nos données
    for d in data:
        # on définit le point
        point = Point(d[0], d[1])
        # on définit les propriétés
        prop = {'name': d[2]}
        # on écrit l'entité
        out.write(
            {'geometry': mapping(point), 'properties': prop}
        )