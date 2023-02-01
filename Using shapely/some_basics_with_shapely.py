import shapely.wkt as wkt
import shapely.geometry as geometry
from shapely.ops import transform
import pyproj

# quelques opérations de base avec Shapely

# on déclare 2 points
# Montréal
lon_mtl, lat_mtl = -73.561668,45.508888
# Sherbrooke
lon_she, lat_she = -71.888351,45.404476

# créer une géométrie à partir d'un WKT
pt_mtl = wkt.loads(f'POINT({lon_mtl} {lat_mtl})')

# créer une géométrie à partir d'un couple x, y
pt_she = geometry.Point((lon_she,lat_she))

# créer une géométrie à partir d'un json
pt_json = {'type': 'Point', 'coordinates': (lon_mtl, lat_mtl)}
pt_mtl2 = geometry.shape(pt_json)

# créer une ligne à partir d'une liste de valeurs
line = [(lon_mtl, lat_mtl), (lon_she, lat_she)]
line_mtl_she = geometry.LineString(line)

# créer une ligne à partir d'une liste de points
line2 = [pt_mtl, pt_she]
line_mtl_she2 = geometry.LineString(line2)

# récupérer le type de la géométrie
print(line_mtl_she2.geom_type)

# parcourir les points
for pt in line_mtl_she2.coords:
    print(pt)

# récupérer la boîte englobante
print(line_mtl_she.bounds)

# créer une géométrie à partir des bornes
poly = geometry.box(*line_mtl_she.bounds)
print(poly)

# vérifier si un point se trouve dans la géométrie
print(poly.contains(poly.centroid))

# reprojeter
crs1 = pyproj.CRS('EPSG:4326')
crs2 = pyproj.CRS('EPSG:6622')

trans = pyproj.Transformer.from_crs(crs1, crs2).transform
polyproj = transform(trans, poly)
print(polyproj)