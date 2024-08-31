'''
Approch:
Comparing the first and Second frames Based on the differences It Find the Movements
'''

import cv2 as cv
import numpy as np

cap = cv.VideoCapture('walking.mp4')

# Frame 1
ret , frame1 = cap.read()
ret , frame2 = cap.read()

while cap.isOpened():
    #Finding The Difference
    diff = cv.absdiff(frame1,frame2)

    # Convert the Diff into Gray Scale
    gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)

    # Add Blur to it 
    blur = cv.GaussianBlur(gray,(5,5),0)

    # Calculate the Threshold
    _, thresh = cv.threshold(blur,20,255,cv.THRESH_BINARY)

    
    # Craete the Dilate
    dilated = cv.dilate(thresh,None,iterations=3)

    # Contour 
    contours , _ = cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    # Draw the Contours
    # cv.drawContours(frame1,coutours,-1,(0,255,0),2)

    for contour in contours:
        (x,y,w,h) = cv.boundingRect(contour)

        # if cv.contourArea(contour)<700:
        #     continue
        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        

        
    
    cv.imshow('feed',frame1)
    frame1=frame2
    ret,frame2 = cap.read()

    if cv.waitKey(40) ==27:
        break
    
cv.destroyAllWindows()
cap.release()

