####
# Author: Austin Crane
# Date: Nov 14, 2016

import numpy as np
import cv2

img = cv2.imread('../../assets/football.jpg', cv2.IMREAD_GRAYSCALE)

# write grayscalled image to output dir
cv2.imwrite('output/football_gray.jpg', img)
