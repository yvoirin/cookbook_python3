# -*- coding: utf-8 -*-
__author__ = 'voirin'

# importer GLOB
import glob
# définir un répertoire à explorer
directory_to_explore = r'C:\data'
# on récupère tous les fichiers du répertoire
files = glob.glob(directory_to_explore + '\*.*')
# on parcourt les fichiers trouvés
for file in files:
    # chemin du fichier
    print(file)
