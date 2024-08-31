import numpy as np
import cv2 as cv


'''
What are the events inside the cv2
events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON',
'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY',
'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP',
'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP',
'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL',
'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
''' 


# Printing The Coordinates in the image
def events(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv.FONT_HERSHEY_COMPLEX
        strxy = str(x)+' , ' +str(y)
        cv.putText(img,strxy,(x,y),font,1,(255,255,0),2)
        cv.imshow('image',img)
    if event ==cv.EVENT_RBUTTONDOWN:
        blue = str(img[x,y,0])
        green = str(img[x,y,1])
        red = str(img[x,y,2])
        font = cv.FONT_HERSHEY_COMPLEX
        cv.putText(img,blue,(x,y),font,1,(255,0,0),2)
        cv.putText(img,green,(x+1,y),font,1,(0,255,0),2)
        cv.putText(img,red,(x-1,y),font,1,(0,0,255),2)
        cv.imshow('image',img)
        
        
# Draw a Linw B/w 2 Axis 
def events1(event,x,y,flag,params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,y)
        points.append((x,y))
        if len(points) >=2:
            cv.line(img,points[-1],points[-2],(255,0,0),5)
        cv.imshow('image',img)



img = np.zeros((512,512,3),np.uint8)
img = cv.imread('helloman.jpg')
points = []
cv.imshow('image',img)
cv.setMouseCallback('image',events) # We Change the events functions
cv.waitKey(0)
cv.destroyAllWindows()
