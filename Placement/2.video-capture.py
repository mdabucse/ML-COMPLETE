import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.isOpened()) # It Returns the Camera is Available or Not
fourcc = cv.VideoWriter_fourcc(*'XVID') # These codes are used to compress the audio and video in that captured file
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))# To save the captured 

while True:
    ret, frame = cap.read()
    if ret:
        gray_change = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        out.write(frame)
        cv.imshow('Live Video Gray',gray_change)
        cv.imshow('Live Video Color',frame)
        if cv.waitKey(1) == 27:
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
    