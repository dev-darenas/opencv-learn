# https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
import cv2 as cv

vid = cv.VideoCapture(0)

while (True):
  # Capture the video frame
  # by frame
  ret, frame = vid.read()
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  canny = cv.Canny(frame, 100, 175)
  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

  cv.imshow('Video', frame)
  cv.imshow('Video Gray', gray)
  cv.imshow('Video Canny', canny)
  cv.imshow('Video Hsv', hsv)

  if cv.waitKey(0) & 0xFF == ord('q'):
      break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
