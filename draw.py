import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# 2. draw rectangle
start_point = (5, 5)
end_point   = (220, 220)
color       = (255, 0, 0)
thickness   = 5

# cv.rectangle(blank, start_point, end_point, color, thickness)
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), color, thickness)
#cv.imshow('Rectangle', blank)

# 3. draw a circle
# center_coordinates = (120, 50)
center_coordinates = (blank.shape[1]//2, blank.shape[0]//2)
radius             = 100
color              = (255, 255, 0)
thickness          = 10

cv.circle(blank, center_coordinates, radius, color, thickness)
# cv.imshow('Circle', blank)

# 4. draw a line
start_point = (0, 0)
end_point   = (500, 500)
color       = (0, 255, 255)
thickness   = 9

cv.line(blank, start_point, end_point, color, thickness)
#cv.imshow('Line', blank)

# 5. Draw a text
font      = cv.FONT_HERSHEY_SIMPLEX
org       = (50, 50)
fontScale = 1
color     = (255, 0, 255)
thickness = 2
text      = 'Im the fucking master!!'

cv.putText(blank, text, org, font, fontScale, color, thickness, cv.LINE_AA, False)
cv.putText(blank, text, org, font, fontScale, color, thickness, cv.LINE_AA, True)
cv.imshow('Text', blank)

# press 0 to exit
cv.waitKey(0)

