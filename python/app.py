import cv2
import numpy as np
from matplotlib import pyplot as plt

import os, sys
RESOURCES_DIR = os.path.join('..', 'resources')
melee_img = os.path.join(RESOURCES_DIR, 'meleeGO.jpg')
smash4_img = os.path.join(RESOURCES_DIR, 'smash4GO.jpg')

img = cv2.imread(melee_img, 0)
edges = cv2.Canny(img, 200, 500)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()