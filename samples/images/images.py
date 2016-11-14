####
# Author: Austin Crane
# Date: Nov 14, 2016

import numpy as np
import cv2

# read image from local directory
## Reading Options
## IMREAD_COLOR => color
## IMREAD_GRAYSCALE => gray scale
## IMREAD_UNCHANGED => read like normal
img_original = cv2.imread('../../assets/football.jpg', cv2.IMREAD_COLOR)
img_black_white = cv2.imread('../../assets/football.jpg', cv2.IMREAD_GRAYSCALE)

# show the image on screen
cv2.imshow('Original', img_original)
cv2.imshow('Gray Scale', img_black_white)

# wait for esc key to be hit and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
