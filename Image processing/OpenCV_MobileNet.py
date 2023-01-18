#
import cv2
import matplotlib.pyplot as plt
import numpy as np

# lire une image
img = cv2.imread(r'data/lenna.png')
rows, cols, bands = img.shape
# définir une architecture (les fichiers ne sont pas fournis)
model_architecture = 'mobilenet/frozen_inference_graph.pb'
config = 'mobilenet/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
framework = 'TensorFlow'

# définir les classes
with open('mobilenet/labels.txt', 'r') as f:
    class_names = f.read().split('\n')

# prétraiter l'image pour le réseau
blob = cv2.dnn.blobFromImage(img, 1.0 / 127.5, (320, 320), [127.5, 127.5, 127.5])

# on va créer le réseau
model = cv2.dnn.readNet(model_architecture, config, framework)
# on introduit l'image
model.setInput(blob)
# on récupère la sortie
output = model.forward()
# on définit une liste de couleur pour les classes
colours = np.random.uniform(0, 255, size=(len(class_names), 3))
# dans la sortie on va récupérer l'activation
for detection in output[0, 0, :, :]:
    # detection contient la classe, la confiance, et la boite englobante
    confidence = detection[2]
    # si la confiance est plus de 50 %
    if confidence > .5:
        # on récupère la classe
        class_id = detection[1]
        # le nom de la classe
        class_name = class_names[int(class_id)-1]
        # la couleur
        color = colours[int(class_id)]
        # on calcule la boite en fonction de la taille de l'image
        box_x = detection[3] * cols
        box_y = detection[4] * rows
        box_width = detection[5] * cols
        box_height = detection[6] * rows
        # on dessine le rectangle
        cv2.rectangle(img, (int(box_x), int(box_y)), (int(box_width), int(box_height)), color, 2)
        # on inscrit le texte
        cv2.putText(img, class_name, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

# afficher l'image avec Matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
