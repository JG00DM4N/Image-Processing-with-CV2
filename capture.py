import cv2, time

video=cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    check, frame = video.read()



    #time.sleep(3)
    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(2)

    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()