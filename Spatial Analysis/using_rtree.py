# on importe les libs
import fiona
import shapely.wkt
import pyproj
from shapely.ops import transform
from shapely.geometry import shape
import time
from datetime import timedelta
import rtree

# on va calculer le temps écoulé
start = time.time()
# on a besoin de reprojeter les géométries
crs1 = pyproj.CRS('EPSG:4326')
crs2 = pyproj.CRS('EPSG:3348')

trans = pyproj.Transformer.from_proj(crs1, crs2, always_xy=True).transform
# il s'agit d'un fichier avec 470 000 entités
filename = r'sample.shp'

# on souhaite connaître les entités qui se trouvent
# dans un voisinage de 1000 m des points suivants
pts = [
    (45.426719, -79.666045), 
    (44.376845, -76.659057), 
    (43.158296, -81.696775),
    (42.213166, -82.436977)
    ]
# on va créer les buffers
buffers = []

for lat, lon in pts:
    point = shapely.wkt.loads(f'POINT({lon} {lat})')
    pointproj = transform(trans, point )
    poly = pointproj.buffer(1000)
    buffers.append(poly)

# avec rtree, on doit créer un index spatial
# il s'agit de définit un identifiant pour une certaine
# région (en général, on associe un FID avec un rectangle)
def generateFidx(collection):
    for fid, feature in collection.items():
        geometry = shape(feature['geometry'])
        yield((fid, geometry.bounds, None))

# on va récupérer la liste des entités d'intérêt
fids = []
# on ouvre le fichier avec fiona
with fiona.open(filename) as src:
    # on va créer l'index spatiale
    # c'est coûteux mais cela peut rapporter gros, si on 
    # doit effectuer plusieurs fois l'analyse de la couche
    # comme dans le cas présent
    idx = rtree.index.Index(generateFidx(src))
    # une fois l'index créé, on peut faire notre analyse
    # pour chaque buffer
    for buff in buffers:
        # on va déjà récupérer les identifiants qui sont concernés par la zone
        # géographique
        tmp_fids = [int(i) for i in idx.intersection(buff.bounds)]
        # ensuite on va récupérer les entités qui sont réellement dans le buffer
        fids += [fid for fid in tmp_fids if buff.contains(shape(src[fid]['geometry']))]
    
    # traditionnellement, on ferait une boucle sur les entités
    # et ensuite une boucle sur les buffers
    # for fid, feature in src.items():
    #     geometry = shape(feature['geometry'])
    #     for buff in buffers:
    #         if buff.contains(shape(feature['geometry'])):
    #             fids.append(fid)

    
# on a effectivement les identifiants        
print(fids)

# on calcule le temps écoulé
elapsed = time.time() - start
print(str(timedelta(seconds=elapsed)))

# la méthode traditionnelle donnait un résultat en 46.80 s
# la méthode rtree donnait le même résultat en 34.96 s (1/4 de temps moins)