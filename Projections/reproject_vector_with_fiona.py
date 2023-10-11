import fiona

# afficher la version de fiona
print(fiona.__version__)

import pyproj
from shapely.geometry import shape, mapping
from fiona.crs import from_epsg
from shapely.ops import transform
# Chemin vers le fichier Shapefile source
source_shapefile_path = r'../data/mask_satellite.shp'
# Spécifiez la projection cible
target_crs = from_epsg(4326) # WGS 84 (EPSG:4326)
# Chemin vers le fichier Shapefile cible
target_shapefile_path = r'../data/mask_satellite_4326.shp'

# Ouvrez le fichier source en mode lecture
with fiona.open(source_shapefile_path, 'r') as src:
    # Ouvrez le fichier cible en mode écriture et spécifiez la nouvelle projection
    with fiona.open(target_shapefile_path, 'w', 'ESRI Shapefile',
        schema=src.schema, crs=target_crs) as dst:
        # Utilisez pyproj pour effectuer la reprojection des géométries
        project = pyproj.Transformer.from_crs(src.crs, target_crs, always_xy=True).transform
        for feature in src:
            geom = shape(feature['geometry'])
            # Appliquez la transformation de projection
            reprojected_geom = transform(project, geom)
            # Écrivez l'entité dans le fichier cible
            feature['geometry'] = mapping(shape(reprojected_geom))

            dst.write(feature)
            # si cette dernière ligne pose problème (sur colab), essayez plutôt :
            # dst.write({'geometry': mapping(reprojected_geom), 'properties':feature['properties']})