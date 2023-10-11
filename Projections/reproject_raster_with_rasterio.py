import numpy as np
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
# image en entrée
source_image_path = r'../data/mask_satellite.tiff'
# crs de sortie
dst_crs = 'EPSG:4326'
# ouverture de l'image
with rasterio.open(source_image_path) as src:
    # calcul de la transformation
    transform, width, height = calculate_default_transform(
    src.crs, dst_crs, src.width, src.height, *src.bounds)
    kwargs = src.meta.copy()
    kwargs.update({
    'crs': dst_crs,
    'transform': transform,
    'width': width,
    'height': height
    })

    # création de l'image de sortie
    with rasterio.open(r'../data/mask_satellite_4326.tiff', 'w', **kwargs) as dst:
        for i in range(1, src.count + 1):
            reproject(
            source=rasterio.band(src, i),
            destination=rasterio.band(dst, i),
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=transform,
            dst_crs=dst_crs,
            resampling=Resampling.nearest)