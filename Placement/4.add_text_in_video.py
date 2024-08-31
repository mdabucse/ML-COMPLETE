import cv2 as cv
import datetime
cap = cv.VideoCapture(0)
print(cap.isOpened()) # It Returns the Camera is Available or Not
while True:
    ret, frame = cap.read()
    if ret:
        font = cv.FONT_HERSHEY_COMPLEX
        date_t = str(datetime.datetime.now())
        cv.putText(frame,date_t,(10,50),font,1,(255,0,0),2)
        cv.imshow('Live Video Color',frame)
        if cv.waitKey(1) == 27:
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
    