import cv2
import numpy as np

img_1 = cv2.imread("Images/cards.jpg")
img_2 = cv2.imread("Images/cards2.jpg")

resized_img = cv2.resize(img_2,(477,500))

stack = np.hstack((img_1,resized_img))
stack_2 = np.vstack((img_1,resized_img))




# cv2.imshow("Image 1",img_1)
# cv2.imshow("Image 2",resized_img)
cv2.imshow("Stack",stack_2)
cv2.waitKey(0)