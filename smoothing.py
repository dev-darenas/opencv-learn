import cv2 as cv

# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
img = cv.imread('photos/cat4k.jpeg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (7,7))
#cv.imshow('Cats Average', average)

# GaussianBlur
Gblur = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Cats Gaussian', Gblur)

# Mediam Blur
mediam = cv.medianBlur(img, 7)
cv.imshow('Cats Mediam', mediam)

# Bilateral Blur
bilateralBlur = cv.bilateralFilter(img, 5, 75, 75)
cv.imshow('Cats Bilateral', bilateralBlur)

# press 0 to exit
cv.waitKey(0)
cv.destroyAllWindows()
