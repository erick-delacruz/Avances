import cv2

image = cv2.imread("MV2.PNG")
cv2.imshow("original",image)
cv2.waitKey(0)

print(image.shape)


#crop1 = image[105:169, 106:216]
#cv2.imshow("cropped",crop1)
#cv2.waitKey(0)
#cv2.imwrite("c1.png", crop1)


#crop2 = image[105:169, 225:325]
#cv2.imshow("crop2", crop2)
#cv2.waitKey(0)
#cv2.imwrite("c2.png", crop2)

#crop3 = image[105:169, 335:435]
#cv2.imshow("crop3", crop3)
#cv2.waitKey(0)
#cv2.imwrite("c3.png", crop3)

#crop4 = image[174:235, 225:325]
#cv2.imshow("crop4", crop4)
#cv2.waitKey(0)
#cv2.imwrite("c4.png", crop4)

crop5 = image[241:291, 120:210]
cv2.imshow("crop5", crop5)
cv2.waitKey(0)
cv2.imwrite("c5.png", crop5)

#crop6 = image[241:300, 225:325]
#cv2.imshow("crop6", crop6)
#cv2.waitKey(0)
#cv2.imwrite("c6.png", crop6)

#crop7 = image[308:361, 71:146]
#cv2.imshow("crop7", crop7)
#cv2.waitKey(0)
#cv2.imwrite("c7.png", crop7)

#crop8 = image[308:361, 162:236]
#cv2.imshow("crop9", crop8)
#cv2.waitKey(0)
#cv2.imwrite("c8.png", crop8)

crop9 = image[308:361, 252:325]
cv2.imshow("crop9", crop9)
cv2.waitKey(0)
cv2.imwrite("c9.png", crop9)

#crop10 = image[311:361, 335:412]
#cv2.imshow("crop10", crop10)
#cv2.waitKey(0)
#cv2.imwrite("nombre.png", nombre_de_la_variable)


#cv2.imwrite("nombre.png", nombre_de_la_variable) ESTO GUARDA LA FOTO

imagen_threshold = cv2.imread("c1.png",0)
(ret, thresh) = cv2.threshold(imagen_threshold, 10, 255, cv2.THRESH_OTSU)
print("Threshold selected: ", ret)
cv2.imwrite("./c1_2.png",thresh)

imagen_threshold = cv2.imread("c4_123.jpg",0)
(ret, thresh) = cv2.threshold(imagen_threshold, 10, 255, cv2.THRESH_OTSU)
print("Threshold selected: ", ret)
cv2.imwrite("./c4_123_123.png",thresh)

imagen_threshold = cv2.imread("my-sharpenedC5_3.jpg",0)
(ret, thresh) = cv2.threshold(imagen_threshold, 10, 255, cv2.THRESH_OTSU)
print("Threshold selected: ", ret)
cv2.imwrite("./c5_2_5.png",thresh)

imagen_threshold = cv2.imread("c6.png",0)
(ret, thresh) = cv2.threshold(imagen_threshold, 10, 255, cv2.THRESH_OTSU)
print("Threshold selected: ", ret)
cv2.imwrite("./c6_2.png",thresh)

imagen_threshold = cv2.imread("c7_sharp.jpg",0)
(ret, thresh) = cv2.threshold(imagen_threshold, 10, 255, cv2.THRESH_OTSU)
print("Threshold selected: ", ret)
cv2.imwrite("./c7_2.png",thresh) 

def cortes(imagen, horizontal, vertical): #Recordar que horizontal es eje Y, vert = X
    pass
