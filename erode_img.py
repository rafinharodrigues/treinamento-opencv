import cv2
import numpy as np


img = cv2.imread("Images/car.jpg")

edge = cv2.Canny(img,50,100)

kernel_dilate = np.ones((5,5),np.uint8)
dilate = cv2.dilate(edge,kernel=kernel_dilate,iterations=1)

kernel_erode = np.ones((6,6),np.uint8)
erode = cv2.erode(dilate,kernel=kernel_erode,iterations=1)




cv2.imshow("Original Image", img)
cv2.imshow("Dilate Imgae", dilate)
cv2.imshow("Erode Image",erode)
cv2.waitKey(0)