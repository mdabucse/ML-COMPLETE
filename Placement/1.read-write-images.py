import cv2 as cv

img = cv.imread(r'helloman.jpg',0)
print(img)
cv.imshow('Window Name',img)
cv.waitKey(0)
cv.destroyAllWindows()

# To store the processed image
cv.imwrite('helloman-gray.jpg',img)