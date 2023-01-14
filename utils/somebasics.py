#1 - détecter quand la boucle FOR a terminé proprement
for i in range(10):
    print(i)
    if i == 30:
        break
else:
    print('ok')

#2 - récupérer des variables grâce à un tableau
ma_liste = [1,2,3,4]
a, b, c, d = ma_liste

print(c)

#3 - trouver les n plus petit ou plus grands éléments d'une liste
import heapq
ma_liste = [1,2,3,4]
print(heapq.nsmallest(2, ma_liste))
print(heapq.nlargest(2, ma_liste))

#4 - transformer un texte déclarant une liste en une vraie liste
import ast
mon_texte = "[1,2,3,4]"
ma_liste = ast.literal_eval(mon_texte)
print(ma_liste[2])

#5 - compter le nombre d'éléments d'une liste
from collections import Counter
ma_liste = [[1],[2,3],[4],[1,2]]
flatten = [x for sub in ma_liste for x in sub]
resu = Counter(flatten)
print(resu)

#6 - faire des permutations, des combinaisons et des produits de listes
from itertools import permutations, combinations, product
ma_liste = [1,2,3]
resu = permutations(ma_liste)
print(list(resu))

resu = combinations(ma_liste, 2)
print(list(resu))

colors = ['P', 'C', 'CO', 'T']
values = [str(i) for i in range(1,11)] + ['V', 'D', 'R']

resu = product(colors, values)
print(len(list(resu)))

#7 - filtrer une liste
ma_liste = [1,2,3]
resu = filter(lambda x:x%2 == 0, ma_liste)
print(list(resu))

#8 - créer une nouvelle liste en appliquant une fonction aux éléments
ma_liste = [1,2,3]
resu = map(lambda x:x*2, ma_liste)
print(list(resu))

#9 - utiliser une abréviation pour les conditions
a = 10
b = "1" if a == 1 else "0"
print(b)

#10 - détecter si un élément respecte plusieurs conditions ou au moins une condition
value = 13
conditions = [ value < 10, value % 2 == 0]

if any(conditions):
    print('ok')
