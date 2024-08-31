import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

def region_ofinterest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    mask_image = cv.bitwise_and(img, mask)
    return mask_image

def draw_the_line(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
    
    img = cv.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img  # Return the modified image with lines drawn

image = cv.imread('road.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Size of The Image
print(image.shape)
height = image.shape[0]
width = image.shape[1]

# Region of Interest -> What are the Coordinates need for finding the road lanes
region_of_interest_vertices = [
    (0, height),
    (width // 2, height // 2),
    (width, height)
]

gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
canny_image = cv.Canny(gray_image, 100, 200)
cropped_image = region_ofinterest(canny_image, np.array([region_of_interest_vertices], np.int32))
lines = cv.HoughLinesP(cropped_image,
                       rho=6,
                       theta=np.pi/60,
                       threshold=160,
                       lines=np.array([]),
                       minLineLength=40,
                       maxLineGap=25)

image_with_lines = draw_the_line(image, lines)

plt.imshow(image_with_lines)
plt.show()

cv.waitKey()
cv.destroyAllWindows()
