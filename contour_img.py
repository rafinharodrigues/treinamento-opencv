import cv2

img = cv2.imread("Images/shapes.png")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge_img = cv2.Canny(gray_img,100,150)

contour, hierarchy = cv2.findContours(edge_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

result = cv2.drawContours(img,contour,-1,(255,0,0),3)



# cv2.imshow("Original Image",img)
cv2.imshow("Edge Image",edge_img)
cv2.imshow("Contour Image",result)
cv2.waitKey(0)