import cv2
import numpy as np
from matplotlib import pyplot as plt

import os, sys
RESOURCES_DIR = os.path.join('..', 'resources')
melee_img = os.path.join(RESOURCES_DIR, 'meleeGO.jpg')
smash4_img = os.path.join(RESOURCES_DIR, 'smash4GO.jpg')


#read image into cv2 and crop area with GO! text
img = cv2.imread(melee_img, 0)
cropped_img = img[200:800, 450:1550]

# optional show cropped image
#cv2.imshow("lul", cropped_img)
#cv2.waitKey(0)

#use canny algo to get edges of an image with a low and high threshold
edges = cv2.Canny(cropped_img, 250, 550)

#optional show original vs cropped image
"""
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
"""

cv2.imshow("helloworldlul", edges)
cv2.waitKey(0)
cv2.imwrite('meleeGOedges.jpg', edges)

#plt.show()