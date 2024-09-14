import cv2

# img = cv2.imread("Images/face.png")

# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# classifier = cv2.CascadeClassifier("classifiers/haarcascade_frontalface_alt.xml")

# faces = classifier.detectMultiScale(gray_img)

# for x, y, w, h in faces:

#     cv2.rectangle(img,(x,y),(x + w, y + h),(255,0,0),3)


# cv2.imshow("Faces",img)
# cv2.waitKey(0)

img = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("classifiers/haarcascade_frontalface_alt.xml")

while True:

    success, frame = img.read()

    if success:

        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = classifier.detectMultiScale(gray_img,minNeighbors=5)

        for x, y, w, h in faces:

            cv2.rectangle(frame,(x,y),(x + w, y + h),(255,0,0),3)
            cv2.imshow("Faces",frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break



