####
# Author: Austin Crane
# Date: Nov 14, 2016

import numpy as np
import cv2

# read video from file
cap = cv2.VideoCapture('../../assets/football.mov')

# loop forever
while(True):
    # grab image from image capture
    # ret is true/false depending if it was successfully captured
    ret, frame = cap.read()

    # convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # show original
    cv2.imshow('Original', frame)
    # show gray
    cv2.imshow('Gray', gray)


    # wait for quit key 1
    if cv2.waitKey(1) & 0xFF == ord('1'):
        # break out of the loop
        break

# free up the camera
cap.release()
cv2.destroyAllWindows()
