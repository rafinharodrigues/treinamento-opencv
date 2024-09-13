import cv2


img = cv2.imread("Images/cards.jpg")

print(img.shape)
print(img.shape[0]*img.shape[1]*img.shape[2])

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

resized_img = cv2.resize(gray_img,(400,300))

print(resized_img.shape)
print(resized_img.shape[0]*resized_img.shape[1])



cv2.imshow("Original image",img)
cv2.imshow("Resized image",resized_img)
cv2.waitKey(0)
