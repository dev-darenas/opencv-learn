import cv2 as cv
import numpy as np

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cats', img)

blankImg = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blankImg)

## findContours ##
# im = cv.imread('test.jpg')
# imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(imgray, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
### ### ### ### ### ###

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Cat Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Cat Canny', canny)

ret, thresh = cv.threshold(gray, 127, 255, 0)
# cv.imshow('Cat thresh', thresh)

# contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

# Draw contours
cv.drawContours(blankImg, contours, -1, (255,0,0), 1)
cv.imshow('Cat thresh', blankImg)

# press 0 to exit
cv.waitKey(0)
cv.destroyAllWindows()
