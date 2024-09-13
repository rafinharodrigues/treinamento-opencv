import cv2
import numpy as np

img = cv2.imread("Images/documentscanner2.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thd1, thd2 = 100, 150

edges = cv2.Canny(gray_img,thd1,thd2)

contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

contour_area = 0
for index, contour in enumerate(contours):

    if cv2.contourArea(contour) >= contour_area:
        index_contour = index
        contour_area = cv2.contourArea(contour)
    else:
        continue


img = cv2.drawContours(img,contours[index_contour],-1,(0,0,255),2)


cv2.imshow("Image",img)
cv2.waitKey(0)