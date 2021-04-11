import cv2 as cv
import numpy as np

img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

# Translation
def translate(img, x, y):
  transMat   = np.float32([[1, 0, x], [0, 1, y]])
  dimentions = (img.shape[1], img.shape[0])
  return cv.warpAffine(img, transMat, dimentions)

# -x -> left
# -y -> up
# x -> right
# y -> down

# translated = translate(img, 100, 100)
# cv.imshow('Translate', translated)


#Rotation
def rotation(img, angle, rotPoint=None):
  (height, width) = img.shape[:2]

  if rotPoint is None:
    rotPoint = (width//2, height//2)

  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
  dimentions = (width, height)
  
  return cv.warpAffine(img, rotMat, dimentions)

#rotated = rotation(img, 45)
#cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (100, 100), interpolation=cv.INTER_AREA)
#cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 2)
#cv.imshow('Flipp', flip)

# Cropping
cropped = img[100:200, 200:300]
cv.imshow('Cropped', cropped)

# press 0 to exit
cv.waitKey(0)
cv.destroyAllWindows()
