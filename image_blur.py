import cv2

img = cv2.imread("Images/face.png")

blur_img = cv2.blur(img,(29,29))
blur2_img = cv2.GaussianBlur(img,(29,29),0)
blur3_img = cv2.medianBlur(img,25)


# cv2.imshow("Original Image",img)
cv2.imshow("Blur Image",blur_img)
cv2.imshow("GaussianBlur Image",blur2_img)
cv2.imshow("MedianBlur Image",blur3_img)
cv2.waitKey(0)


