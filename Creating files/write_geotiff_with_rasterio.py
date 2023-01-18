# j'importe mes libs
import numpy as np
#import matplotlib.pyplot as plt
import rasterio
from rasterio.transform import Affine

# on invente une grille à sauvegarder
x = np.linspace(-4.0, 4.0, 240)
y = np.linspace(-3.0, 3.0, 180)
# on définit une grille
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)

# si on veut voir la matrice
# plt.imshow(Z)
# plt.show()

# on doit déterminer la transformation (Géoréférence)
# ici, on doit la calculer car on a inventé la donnée
# la résolution de notre image
res = (x[-1] - x[0] / 240)
# la transformation est une matrice impliquant
# le pixel 0,0 et le déplacement en X et Y (taille des pixels)
transform = Affine.translation(x[0] - res/2, y[0] - res/2) * Affine.scale(res, res)

# on peut créer notre image à partir de la matrice Z
output = rasterio.open('resu_rasterio.tiff', 'w', driver='GTiff',
                       height=Z.shape[0], width=Z.shape[1],
                       count=1, dtype=Z.dtype, crs='+proj=latlong',
                       transform=transform)
# on écrit la matrice dans la bande 1
output.write(Z, 1)
# on ferme le fichier
output.close()

