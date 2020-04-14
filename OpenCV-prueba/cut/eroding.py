import cv2
import numpy as np

img = cv2.imread('c7_2.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imwrite('c7_22.png', img)