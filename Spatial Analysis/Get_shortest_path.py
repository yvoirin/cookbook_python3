# -*- coding: utf-8 -*-
__author__ = 'voirin'

# j'importe networkx
import networkx as nx
# j'importe pyplot
import matplotlib.pyplot as plt
# j'importe la lib
import ogr
# je déclare le fichier à lire (ajuster le chemin selon votre machine)
# attention votre fichier de rues doit contenir des géométries simples (non multiples)
filename = r'../data/Segments_de_rue_singlepart.shp'
# je déclare un driver SHP
driver = ogr.GetDriverByName('ESRI Shapefile')
# j'ouvre le fichier
datasource = driver.Open(filename)
# je vais chercher la couche
layer = datasource.GetLayer()

# je vais créer 2 listes
# nodes = liste des noeuds
# Noeud = extrêmités de chaque ligne. Le premier et le dernier point.
# edges = liste des chemins
# Chemin = lien possible entre 2 noeuds
nodes = []
edges = []

# je parcours les entités
for feature in layer:
    # je récupère la géométrie
    geom = feature.GetGeometryRef().Clone()
    # on va définir les noeuds du graphe comme les positions x, y
    # premier point de la géométrie (coordonnées)
    first = geom.GetPoint(0)[:-1]
    # dernier point de la géométrie (coordonnées)
    last = geom.GetPoint(geom.GetPointCount()-1)[:-1]
    # on ajoute le point si il n'existe pas dans la liste
    if first not in nodes:
        nodes.append(first)
    # on ajoute le point si il n'existe pas dans la liste
    if last not in nodes:
        nodes.append(last)
    # on ajoute le chemin avec l'information de longueur
    # cette information pourra être utilisée comme poids
    # dans la détermination du chemin le plus court
    # On peut ajouter d'autres informations utiles pour la suite, comme
    # le nom du tronçon
    edges.append((first, last, {'length': geom.Length(), 'name': feature.GetField('TOPONYMIE')}))

# on va créer un graphe
G = nx.Graph()
# on ajoute les noeuds
G.add_nodes_from(nodes)
# on ajoute les arrêtes
G.add_edges_from(edges)


# on peut définir deux points d'intérêt
# sur le territoire
# point de départ
start = 177295.167,5014043.673
pt_start = ogr.Geometry(ogr.wkbPoint)
pt_start.AddPoint(start[0], start[1])
# point d'arrivée
end = 210083.328,5036857.932
pt_end = ogr.Geometry(ogr.wkbPoint)
pt_end.AddPoint(end[0], end[1])
# on doit trouver les noeuds du graphe
# qui sont proches de ces points
node_start, dist = None, 100000
node_end, dist2 = None, 100000
# on parcourt les noeuds
for n in G.nodes():
    # pour chaque point on calcule la distance
    pt = ogr.Geometry(ogr.wkbPoint)
    pt.AddPoint(n[0], n[1])
    # distance entre le neoud et le point de départ
    dist_from_start = pt.Distance(pt_start)
    # distance entre le neoud et le point d'arrivée
    dist_from_end = pt.Distance(pt_end)
    # on conserve le noeud s'il est encore plus proche que
    # l'ancien noeud
    if dist_from_start < dist:
        node_start = n
        dist = dist_from_start
    if dist_from_end < dist2:
        node_end = n
        dist2 = dist_from_end
# on a trouvé le noeud de départ et le noeud d'arrivée
# correspondant au trajet à effectuer
print("Le noeud de départ est : %s à une distance de %.2f m" % (node_start, dist))
print("Le noeud d'arrivée est : %s à une distance de %.2f m" % (node_end, dist2))

# je cherche le chemin à parcourir (avec le poid le plus petit,
# autrement dit la longueur la plus petite)
shortpath = nx.shortest_path(G, source=node_start, target=node_end, weight='length')
# la liste des chemins à parcourir
edges_for_short_path = []
# On parcourt le chemin le plus court
for index,node in enumerate(shortpath[:-1]):
    # on peut récupérer les infos de chaque tronçon
    data = G.get_edge_data(node, shortpath[index+1])

    print("Chemin entre : %s -> %s -- Appelé : %s" % (node, shortpath[index+1], data['name']))

    edges_for_short_path.append((node, shortpath[index+1]))
# pour dessiner le graphe on doit définir un dictionnaire
pos = {v: v for k,v in enumerate(G.nodes())}
# on dessine les noeuds
nx.draw_networkx_nodes(G, pos, node_size=0.1, node_color="red")
# on dessine les chemins (simplifiés)
nx.draw_networkx_edges(G,pos, edge_color= "black", width=1)
# on dessine le chemin à parcourir en vert
nx.draw_networkx_edges(G,pos, edgelist=edges_for_short_path, edge_color= "green", width=3)

# on dessine le graphe
ax = plt.gca()
ax.margins(0.01)
plt.axis("off")
plt.show()