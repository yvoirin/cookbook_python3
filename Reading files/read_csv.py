# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe CSV
import csv
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
# on affiche les données
print(data)
print(days)