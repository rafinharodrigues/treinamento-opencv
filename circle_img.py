import cv2


img = cv2.imread("Images/cards.jpg")

cv2.circle(img,(200,200),100,(0,255,0),3)

cv2.circle(img,(150,200),50,(255,0,0),3)



cv2.imshow("Image",img)
cv2.waitKey(0)