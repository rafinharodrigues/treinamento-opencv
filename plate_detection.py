import cv2


cap = cv2.VideoCapture("Videos/demo.mp4")
classifier = cv2.CascadeClassifier("classifiers/haarcascade_russian_plate_number.xml")


while True:

    ret, frame = cap.read()

    if ret:

        plate = classifier.detectMultiScale(frame,scaleFactor=1.2,minNeighbors=10)

        for x, y, w, h in plate:

            cv2.rectangle(frame,(x,y),(x + w, y + h),(255,0,0),3)
            cv2.putText(frame,"Plate Detected",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
            
        cv2.imshow("Plate Detection",frame)

        if cv2.waitKey(25) & 0xFF==ord('q'):
            break
    else:
        break