# j'importe PIL et random
from PIL import Image
import random

# je définis le fichier à lire
filename = r'../data/lenna.png'
# ma taille de tuile pour le découpage
tile = 32
# ma liste des zones à découper
regions = []
# j'ouvre l'image
with Image.open(filename) as im:
    # je récupère la taille
    size = im.size
    # je vais créer une image pour la sortie
    resu = Image.new(im.mode, size)
    # je calcule le découpage que je dois faire sur les lignes et colonnes
    cols = range(0, size[0], tile)
    rows = range(0, size[1], tile)
    # voici mes régions
    for r in rows:
        for c in cols:
            regions += [(c, r, c + tile, r + tile)]
    # on va conserver les régions originales
    originalregion = regions.copy()
    # on mélange les régions pour avoir un côté aléatoire
    random.shuffle(regions)
    # je parcours mes régions
    for index,box in enumerate(regions):
        # je cherche la zone originale
        orignBox = originalregion[index]
        # je découpe en fonction d'une zone aléatoire
        region = im.crop(box)
        # je colle la zone découpée à l'endroit original
        resu.paste(region, orignBox)
# le résultat sera comme un patchwork aléatoire
resu.show()
# je peux sauvegarder le résultat
resu.save('resu.png')