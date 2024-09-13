import cv2


img = cv2.imread("Images/face.png")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Imagem Colorida",img)
cv2.imshow("Imagem Cinza",gray_img)
cv2.waitKey(0)