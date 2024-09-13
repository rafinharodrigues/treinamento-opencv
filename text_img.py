import cv2


img = cv2.imread("Images/cards.jpg")

cv2.putText(img,"Curso OpenCV",(100,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,0),2)



cv2.imshow("Image",img)
cv2.waitKey(0)