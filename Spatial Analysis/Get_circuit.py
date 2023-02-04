# -*- coding: utf-8 -*-
__author__ = 'voirin'
__copyright__ = "Copyright 2020"

# j'importe networkx
import networkx as nx
# j'importe pyplot
import matplotlib.pyplot as plt
# j'importe la lib
import ogr, osr

import itertools

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
    speed = feature.GetField('VITESSE')
    seg = feature.GetField('TYPESEGMEN')
    if speed == 0:
        speed = 30
    length = geom.Length()
    time = (1.0) * (length / 1000) / speed
    edges.append((first, last, {'geom': geom,'length': length, 'name': feature.GetField('TOPONYMIE'), 'speed': speed, 'time': time}))

# on va créer un graphe
G = nx.Graph()
# on ajoute les noeuds
G.add_nodes_from(nodes)
# on ajoute les arrêtes
G.add_edges_from(edges)

def getCoordinates(pts):
    pt = ogr.Geometry(ogr.wkbPoint)
    pt.AddPoint(pts[0], pts[1])
    return pt

def getClosestNode(point, G):
    node, distmin = None, 100000
    for n in G.nodes():
        # pour chaque point on calcule la distance
        pt = ogr.Geometry(ogr.wkbPoint)
        pt.AddPoint(n[0], n[1])
        dist = pt.Distance(point)
        if dist < distmin:
            distmin = dist
            node = n
    return node,distmin


def readCollect(filename, G):
    datasource = driver.Open(filename)
    layer = datasource.GetLayer()
    # je vais alimenter cette liste coutries avec les infos du Shapefile
    points = []
    # je parcours les entités
    node_start = None
    node_end = None
    nodes = []
    for feature in layer:
        name = feature.GetField('name')
        geom = feature.GetGeometryRef().Clone()
        #points.append([name, geom])
        node, dist = getClosestNode(geom, G)
        if name == 'start':
            node_start = node
        elif name == 'end':
            node_end = node
        else:
            nodes.append(node)

    return node_start, node_end, nodes


nodestart, nodeend, nodes = readCollect(r'../data/collect_points.shp', G)
# on peut définir deux points d'intérêt
# sur le territoire
# point de départ
# start = 178431.555,5016670.238
# pt_start = getCoordinates(start)
# nodestart, dist0 = getClosestNode(pt_start, G)
#
# # point d'arrivée
# end = 202853.412,5037675.045
# pt_end = getCoordinates(end)
# nodeend, dist5 = getClosestNode(pt_end, G)
#
# step1 = 193439.774,5027323.394
# pt_step1 = getCoordinates(step1)
# nodestep1, dist1 = getClosestNode(pt_step1, G)
#
# step2 = 186940.679,5029132.420
# pt_step2 = getCoordinates(step2)
# nodestep2, dist2 = getClosestNode(pt_step2, G)
#
# step3 = 183255.625,5023269.835
# pt_step3 = getCoordinates(step3)
# nodestep3, dist3 = getClosestNode(pt_step3, G)
allpossiblepath = []
for i in list(itertools.permutations(nodes)):
    path = []
    path.append(nodestart)
    for p in i:
        path.append(p)
    path.append(nodeend)
    print(path)
    allpossiblepath.append(path)

costallpath = []
for path in allpossiblepath:
    cost = 0
    circuit = []
    geometries = []
    for i,p in enumerate(path[:-1]):
        shortpath = nx.shortest_path(G, source=p, target=path[i+1], weight='time')
        circuit.append(shortpath)

        for index, node in enumerate(shortpath[:-1]):
            # on peut récupérer les infos de chaque tronçon
            data = G.get_edge_data(node, shortpath[index + 1])
            geom = data['geom']
            cost += data['length']
            geometries.append(geom)
    print(cost)
    costallpath.append([cost, circuit, geometries])

costallpath.sort(key=lambda item:item[0])

print(costallpath[0])

def savefile(circuits):
    # Je déclare un système de coordonnées (wgs84)
    spatialReference = osr.SpatialReference()
    spatialReference.ImportFromEPSG(32187)

    # je déclare le chemin du fichier à écrire
    path = r'../data/circuits4.shp'
    # je déclare le driver que je veux utiliser
    driver = ogr.GetDriverByName('ESRI Shapefile')
    # je créé un datasource pour mes données
    shapeData = driver.CreateDataSource(path)
    # je créé une couche de points
    layer = shapeData.CreateLayer('customs', spatialReference, ogr.wkbLineString)

    # # je recherche la définition de la couche(attributs)
    layer_defn = layer.GetLayerDefn()
    # # je définis un attribut (nom et type)
    # new_field = ogr.FieldDefn('circuit', ogr.OFTString)
    # # je l'ajoute à la couche
    # layer.CreateField(new_field)


    cnt = 0
    for line in circuits:

        # je déclare mon objet point
        #line = ogr.Geometry(ogr.wkbLineString)
        # for pt in c:
        #     # voici mon point
        #     line.AddPoint(pt[0], pt[1])
        # voici son index
        featureIndex = cnt
        # je créé l'entité avec la définition des attributs
        feature = ogr.Feature(layer_defn)
        # je lui associe une géométrie
        feature.SetGeometry(line)
        # je définis l'index
        feature.SetFID(featureIndex)
        # je vais ajouter la valeur d'un attribut
        #feature.SetField("NAME", p['name'])
        # j'ajoute l'entité a la couche
        layer.CreateFeature(feature)
        cnt += 1

    # je termine l'édition
    shapeData.Destroy()


savefile(costallpath[0][2])