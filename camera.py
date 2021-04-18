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

  haar_cascade = cv.CascadeClassifier('face_detection/haar_face.xml')
  faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

  cv.imshow('Video', frame)
  # cv.imshow('Video Gray', gray)
  cv.imshow('Video Canny', canny)
  cv.imshow('Video Hsv', hsv)

  for (x,y,w,h) in faces_rect:
      cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

  cv.imshow('Detected Faces', frame)

  if cv.waitKey(0) & 0xFF == ord('q'):
      break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
