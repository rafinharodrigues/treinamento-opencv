import cv2
import numpy as np


img = cv2.imread("Images/documentscanner2.jpg")

width, height = 600, 800

pts1 = np.float32([[30,229],[571,151],[133,982],[726,858]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

warp_img = cv2.warpPerspective(img,matrix,(width,height))



cv2.imshow("Original Image",img)
cv2.imshow("Warp Image",warp_img)
cv2.waitKey(0)