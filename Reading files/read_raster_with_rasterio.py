import rasterio
# Ouvrir le fichier raster
with rasterio.open(r"../data/alberta_2011.tiff") as src:
    # Lire la matrice NumPy de la première bande
    raster_matrix = src.read(1)
    # Vous pouvez maintenant manipuler la matrice NumPy selon vos besoins
    print("Matrice NumPy :")
    print(raster_matrix)

## si l'image a plusieurs bandes, on peut les lire toutes en même temps

# Ouvrir le fichier raster
with rasterio.open(r"../data/alberta_2011.tiff") as src:
    # Lire la matrice NumPy de toutes les bandes
    raster_matrix = src.read()
    # Vous pouvez maintenant manipuler la matrice NumPy selon vos besoins
    print("Matrice NumPy :")
    print(raster_matrix)

## si on souhaite lire certaines bandes seulement

# Ouvrir le fichier raster
with rasterio.open(r"../data/alberta_2011.tiff") as src:
    # Lire la matrice NumPy de la première et troisième bande
    raster_matrix = src.read([1, 3]) #assurez-vous que les bandes existent
    # Vous pouvez maintenant manipuler la matrice NumPy selon vos besoins
    print("Matrice NumPy :")
    print(raster_matrix)