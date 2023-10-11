import fiona
import rasterio
from rasterio.features import geometry_mask
from shapely.geometry import shape
# Spécifiez le chemin vers votre fichier Shapefile
shapefile_path = r'../data/mask_satellite.shp'
# Ouvrez le fichier Shapefile en mode lecture
with fiona.open(shapefile_path, 'r') as shapefile:
    print(shapefile.meta)
    # Obtenez la première géométrie du Shapefile
    firstshape = shape(shapefile[0]["geometry"])
    # Obtenez les limites de la géométrie
    bbox = firstshape.bounds

    # la résolution souhaitée du raster en mètres par pixel
    resolution = 10 # 10 mètres
    # Transformation à partir de l'origine, de la résolution et des dimensions
    transform = rasterio.transform.from_origin(bbox[0], bbox[3], resolution, resolution)
    # Dimensions du raster à partir de la transformation
    width = int((bbox[2] - bbox[0]) / resolution)
    height = int((bbox[3] - bbox[1]) / resolution)
    # Masque raster à partir des géométries du Shapefile
    mask = geometry_mask([firstshape], transform=transform, invert=True,
    out_shape=(height, width))
    # Créez un nouveau fichier raster
    with rasterio.open(r'../data/mask_satellite.tiff', 'w', driver='GTiff', height=height,
        width=width, count=1, dtype='uint8', crs=shapefile.crs,
        transform=transform) as dst:
        dst.write(mask, 1)