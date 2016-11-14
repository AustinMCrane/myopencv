####
# Author: Austin Crane
# Date: Nov 14, 2016

import numpy as np
import cv2

img = cv2.imread('../../assets/football.jpg', cv2.IMREAD_COLOR)

# draw text
cv2.putText(img, 'Colts', (10,100),cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('Text', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
