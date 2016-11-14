####
# Author: Austin Crane
# Date: Nov 14, 2016

import numpy as np
import cv2

img = cv2.imread('../../assets/football.jpg', cv2.IMREAD_COLOR)
# draw a line on image
img = cv2.line(img,(0,0),(100,100),(255,0,0),5)


cv2.imshow('Drawing', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
