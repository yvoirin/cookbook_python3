# -*- coding: utf-8 -*-
__author__ = 'voirin'

# on import matplotlib
import matplotlib.pyplot as plt

# on a besoin de 2 séries de données, les X et les Y
# les x peuvent être simplement un suite d'entiers
x = range(0, 20) # ici, on aura une liste de 0 à 19
# les y sont aussi une autre série de valeurs
y = range(20, 0, -1) # on génère une liste de valeur de 20 à 1

# un graphique est simplement la représentation des
# y en fonction de x
plt.plot(x, y, color='r')
# on peut afficher la figure
plt.show()
# ou on peut la sauvegarder
# plt.savefig('mytest.jpg')
