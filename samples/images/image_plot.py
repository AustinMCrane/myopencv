####
# Author: Austin Crane
# Date: Nov 14, 2016

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../../assets/football.jpg', cv2.IMREAD_GRAYSCALE)

# plot with may plot lib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

plt.show()
# write grayscalled image to output dir
