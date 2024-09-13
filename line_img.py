import cv2

img = cv2.imread("Images/cards.jpg")

print(img.shape)

cv2.line(img,(0,0),(477,500),(255,0,0),2)

cv2.line(img,(50,50),(40,80),(0,255,0),2)


cv2.line(img,(100,100),(200,200),(0,0,255),2)



cv2.imshow("Imagem",img)
cv2.waitKey(0)