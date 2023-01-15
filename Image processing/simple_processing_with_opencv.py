# Opérations de base avec OpenCV
import cv2
import matplotlib.pyplot as plt
import numpy as np

# lire une image
img = cv2.imread(r'data/lenna.png')
rows, cols, bands = img.shape

# afficher une image avec OpenCV
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# afficher l'image avec Matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# afficher une bande
band0 = img[:,:,0]
plt.imshow(band0)
plt.show()

# appliquer un masque
mask = np.zeros((rows,cols), np.uint8)
mask[100:350, 100:350] = 255
img_masked = cv2.bitwise_and(img, img, mask=mask)
plt.imshow(cv2.cvtColor(img_masked, cv2.COLOR_BGR2RGB))
plt.show()

# appliquer une transformation
M = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), 180, 1)
img_resu = cv2.warpAffine(img, M, (cols, rows))
plt.imshow(cv2.cvtColor(img_resu, cv2.COLOR_BGR2RGB))
plt.show()
# combiner les images
img_resu2 = cv2.addWeighted(img, 0.3, img_resu, 0.7, 0)
plt.imshow(cv2.cvtColor(img_resu2, cv2.COLOR_BGR2RGB))
plt.show()
# filtrer les images
img_resu3 = cv2.GaussianBlur(img, (25,25), 0)
plt.imshow(cv2.cvtColor(img_resu3, cv2.COLOR_BGR2RGB))
plt.show()

# détecter les contours
#img_resu4 = cv2.Sobel(src=img, ddepth=cv2.CV_8U, dx=1, dy=0, ksize=5)
img_resu4 = cv2.Canny(image=img, threshold1=150, threshold2=300)
plt.imshow(cv2.cvtColor(img_resu4, cv2.COLOR_BGR2RGB))
plt.show()

# faire l'histogramme
color = ('b', 'g', 'r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.show()
