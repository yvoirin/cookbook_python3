# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe pandas
import pandas as pd
# je lis le fichier csv
df = pd.read_csv(r'../data/6eee0ac1-126b-4080-8f8f-dc737d81a704_Data.csv',
                 sep=',', dtype={'Population total': float},
                 usecols=['Time','Time Code','Country Name',
                          'Country Code','Population total',
                          'Population male','Population female'])

# on peut afficher le contenu des premières lignes
# print(df.head())

# La population du Canada en 2019
resu = df[(df['Country Name'] == 'Canada') & (df['Time'] == 2019)]
print(resu['Population total'].values)

# La population du Canada en 2010
resu = df[(df['Country Name'] == 'Canada') & (df['Time'] == 2010)]
print(resu['Population total'].values)

# Le pays avec le plus de population en 2019
# on cherche la position du max
index = df[df['Time'] == 2019]['Population total'].idxmax()
# on affiche le pays
print(df.iloc[index]['Country Name'])

# Calcul de la croissance
# on peut faire une extraction des 2 années
country2019 = df[df['Time'] == 2019]
country2010 = df[df['Time'] == 2010]

# on fait un reset des indices pour pouvoir les comparer
country2010 = country2010.reset_index()
country2019 = country2019.reset_index()

# on peut pacourir les 2 jeux de données
# et on calcul la différence
# on va conserver les données dans une liste
results = []
# on parcourt les jeux de données
for index, row in country2019.iterrows():
    # on récupère le nom et la population
    name = row['Country Name']
    value2019 = row['Population total']
    value2010 = country2010.iloc[index]['Population total']
    # on conserve le nom du pays et sa croissance
    results.append([name, (value2019 - value2010)])

# on pourrait afficher les résultats en ordre croissant
results.sort(key=lambda item:item[1])
for r in results:
    print("%s - Croissance de %.2f" % (r[0], r[1]))