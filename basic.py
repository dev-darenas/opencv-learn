import cv2 as cv

img = cv.imread('photos/cat1.jpg')
cv.imshow('CAT', img)

# converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('GRAY', gray)

# Blur img
blur = cv.GaussianBlur(img, (5,5), 0)
# cv.imshow('Blur Cat', blur)

blur7 = cv.GaussianBlur(img, (7,7), 0)
# cv.imshow('Blur Cat 7', blur7)

# edge cascade
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

canny = cv.Canny(img, 100, 175)
cannyBlur = cv.Canny(blur, 100, 175)

# cv.imshow('Canny', canny)
# cv.imshow('Canny Blur', cannyBlur)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
#cv.imshow('Dilate', dilated)

erode = cv.erode(canny, (3,3), iterations=1)
#cv.imshow('Dilate', erode)


cv.waitKey(0)
