import cv2


img = cv2.imread("Images/car.jpg")


def mouse_callback(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(0,255,0),4)
        cv2.imshow("Image",img)



cv2.imshow("Image",img)
cv2.setMouseCallback("Image",mouse_callback)

cv2.waitKey(0)