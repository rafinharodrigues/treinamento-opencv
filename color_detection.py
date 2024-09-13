import cv2
import numpy as np

# 255, 162, 50 RGB
# 50, 162, 255 BGR
# 16, 205, 255 HSV

img = cv2.imread("Images/lambo.png")

hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# pixel = np.array([[[50,162,255]]],np.uint8)
# print(cv2.cvtColor(pixel,cv2.COLOR_BGR2HSV))

lower_bound = (16-10, 205-30, 255-30) # np.array([[[16-10, 205-30, 255-30]]],np.uint8)
upper_bound = (16+15, 205+15, 255) # np.array([[[16+10, 205+10, 255]]],np.uint8)

mask = cv2.inRange(hsv_img,lower_bound,upper_bound)

result = cv2.bitwise_and(img,img,mask=mask)


cv2.imshow("Original Image",img)
cv2.imshow("HSV Image",hsv_img)
cv2.imshow("Orange Image",result)

cv2.waitKey(0)