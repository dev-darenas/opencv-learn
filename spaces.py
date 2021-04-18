import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/cat1.jpg')
#cv.imshow('Cats', img)

#plt.imshow(img)
#plt.show()

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Cats Gray', gray)

#hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('Cats Hsv', hsv)

#lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('Cats lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('Cats RGB', rgb)

plt.imshow(rgb)
plt.show()

# press 0 to exit
# cv.waitKey(0)
# cv.destroyAllWindows()
