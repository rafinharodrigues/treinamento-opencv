import cv2
import numpy as np


img = cv2.imread("Images/car.jpg")

edge_image = cv2.Canny(img,50,100)

kernel = np.ones((1,1),np.uint8)

dialete = cv2.dilate(edge_image,kernel=kernel,iterations=1)

cv2.imshow("Original Image",img)
cv2.imshow("Edge Image",edge_image)
cv2.imshow("Dilate Image",dialete)
cv2.waitKey(0)