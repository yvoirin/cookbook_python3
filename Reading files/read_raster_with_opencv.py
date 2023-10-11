import cv2
# Ouvrir le fichier raster avec OpenCV
raster_path = r"../data/alberta_2011.tiff"
all_bands = cv2.imread(raster_path, cv2.IMREAD_LOAD_GDAL)
# Vérifier les dimensions de la matrice
height, width, num_bands = all_bands.shape
print(f"Dimensions de la matrice : {height}x{width}x{num_bands}")
# Accéder à une bande spécifique
band_1 = all_bands[:, :, 0] # Première bande
band_2 = all_bands[:, :, 1] # Deuxième bande, etc.
print(band_1)
