import fiona
import rasterio
import rasterio.mask
# Spécifiez le chemin vers votre fichier Shapefile
shapefile_path = r'../data/mask_satellite.shp'
# Ouvrez le fichier Shapefile en mode lecture
with fiona.open(shapefile_path, 'r') as shapefile:
    # Accédez à la première entité géométrique
    geom = shapefile[0]['geometry']
    # Spécifiez le chemin vers votre image raster
    raster_path = r'../data/satellite.tiff'
    # Ouvrez l'image raster en mode lecture
    with rasterio.open(raster_path) as src:
        # Découpez l'image en utilisant la géométrie du Shapefile
        out_image, out_transform = rasterio.mask.mask(src, [geom], crop=True)
        out_meta = src.meta.copy()
        out_meta.update({"driver": "GTiff", "height": out_image.shape[1],
        "width": out_image.shape[2], "transform": out_transform})
        with rasterio.open(r"../data/satellite_clip.tiff", "w", **out_meta) as dest:
            dest.write(out_image)