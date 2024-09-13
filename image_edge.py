import cv2
import numpy as np

img = cv2.imread("Images/car.jpg")

edge_img = cv2.Canny(img,50,150)
edge_img2 = cv2.Canny(img,50,300)

cv2.imshow("Image Original",edge_img2)
cv2.imshow("Image Edge",edge_img)
cv2.waitKey(0)