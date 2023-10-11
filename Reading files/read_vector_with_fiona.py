import fiona
# Spécifiez le chemin vers votre fichier Shapefile
shapefile_path = r'../data/world.shp'
# Ouvrez le fichier Shapefile en mode lecture
with fiona.open(shapefile_path, 'r') as source:
    # Affichez les métadonnées du fichier
    print(source.meta)
    # Parcourez les entités du fichier
    for feature in source:
        # Affichez les attributs de l'entité
        print(feature['properties'])
        # Affichez la géométrie de l'entité (au format GeoJSON)
        print(feature['geometry'])
        # La valeur de l'ID unique de l'entité
        print("ID de l'entité :", feature['id'])