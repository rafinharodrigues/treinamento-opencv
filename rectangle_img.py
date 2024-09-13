import cv2


img = cv2.imread("Images/cards.jpg")

cv2.rectangle(img,(100,100),(300,300),(255,0,0),3)


cv2.imshow("Image",img)
cv2.waitKey(0)