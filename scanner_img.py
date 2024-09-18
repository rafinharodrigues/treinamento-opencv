import cv2
import numpy as np


pts = np.zeros((4,2),int)
count = 0
width, height = 500, 600

def mouse_callback(event, x, y, flags, param):

    global pts
    global count

    if event == cv2.EVENT_LBUTTONDOWN:

        if count < 4:
            pts[count] = x,y
            count += 1
            print(pts)
            cv2.circle(img,(x,y),2,(0,0,255),4)
            cv2.imshow("Image",img)

        if count == 4:
            
            pts1 = np.float32(pts)
            pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

            matrix = cv2.getPerspectiveTransform(pts1,pts2)
            output_img = cv2.warpPerspective(img,matrix,(width,height))

            cv2.imshow("Scanned",output_img)

img = cv2.imread("Images/documentscanner2.jpg")


cv2.imshow("Image",img)
cv2.setMouseCallback("Image",mouse_callback)
cv2.waitKey(0)


254
1125
1591
720

257
717
1119
1587