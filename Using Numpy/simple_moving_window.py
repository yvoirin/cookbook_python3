# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe CSV
import csv
# j'importe numpy
import numpy as np
# j'importe matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
# fichier csv à lire
filename = r'../data/AAPL.csv'
# on récupère 2 infos dans le csv
# les jours
days = []
# les valeurs de clôture de l'action
data = []
# Question 1 - on lit le fichier
with open(filename) as csvfile:
    # on définit le format du csv
    csvreader = csv.reader(csvfile, delimiter=',')
    # on parcourt les lignes
    for index, row in enumerate(csvreader):
        # on ignore l'entête
        if index > 0:
            # on récupère la date
            days.append(row[0])
            # on récupère la valeur de clôture
            data.append(float(row[4]))

# Question #2 - on tranforme en matrice
mat_data = np.array(data)
# on vérifie la taille de la matrice
print(mat_data.shape)
# Question #3 - la moyenne sur 7 jours
# on va simplement faire une convolution de 2 matrices
# une moyenne est simplement une convolution par une matrice de 1 (toutes les valeurs
# ont le même poid)
# on utilise convolve
# notre matrice de 1 sur 7 valeurs -> np.ones(7)
# on doit diviser par le nombre de valeurs pour avoir une moyenne
resu = np.convolve(mat_data, np.ones(7), 'valid') / 7

print(resu)
# on va afficher les dates correspondant aux moyennes
print(days[3:-3])
