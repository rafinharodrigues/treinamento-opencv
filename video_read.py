import cv2


video = cv2.VideoCapture("Videos/2.mp4")

while True:

    success, frame = video.read()

    if success:
        cv2.imshow("Video",frame)

        if cv2.waitKey(50) & 0xFF==ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()