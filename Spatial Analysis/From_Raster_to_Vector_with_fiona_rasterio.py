import rasterio
from rasterio.features import shapes
import fiona
from shapely.geometry import shape, mapping
from fiona.crs import from_string
image_path = r'../data/mask_satellite.tiff'
# Ouvrez l'image raster en mode lecture
with rasterio.open(image_path) as src:
    
    image = src.read(1) # Lisez la première bande de l'image (ou la bande souhaitée)
    # Trouvez les régions (objets) dans l'image
    image_regions = list(shapes(image, mask=None, transform=src.transform))
    shapefile_path = r'../data/mask_satellite_convert.shp' # Spécifiez le chemin de sortie
    # obtenir le système de coordonnées de l'image en epsg
    crs_proj4 = src.crs.to_proj4() # Obtenez le système de coordonnées de l'image
    # Ouvrez le fichier Shapefile en mode écriture
    crs_vector = from_string(crs_proj4) # Convertissez le système de coordonnées
    with fiona.open(shapefile_path, 'w', 'ESRI Shapefile', crs=from_string(crs_proj4),
        schema={'geometry': 'Polygon', 'properties':{}}) as output:
        for geom, _ in image_regions:
            # Enregistrez la géométrie dans le fichier Shapefile
            feature = {'geometry': mapping(shape(geom)), 'properties': {}}
            output.write(feature)