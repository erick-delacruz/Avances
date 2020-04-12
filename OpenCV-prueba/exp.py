import cv2
import pytesseract
import numpy as np
#pytesseract.pytesseract.tesseract_cmd = (
#   r'/usr/local/Cellar/tesseract/3.04.01_1/bin/tesseract')


img = cv2.imread('MV2.PNG')

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)
cv2.waitKey()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', gray)
cv2.waitKey()

gray_inv = cv2.bitwise_not(gray)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', gray_inv)
cv2.waitKey()

edges = cv2.Canny(gray, 50, 150)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', edges)
cv2.waitKey()

# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('image', img)
# cv2.waitKey()

# img = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)

# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('image', img)
# cv2.waitKey()

#text = pytesseract.image_to_string(gray)
#print(text)

img = cv2.imread('c1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)

img = cv2.imread('c2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)

img = cv2.imread('c3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)

img = cv2.imread('c4.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)

img = cv2.imread('c5.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)

img = cv2.imread('c6.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)

img = cv2.imread('c7.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)

img = cv2.imread('c8.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)

img = cv2.imread('c9.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)
