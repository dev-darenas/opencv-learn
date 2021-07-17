import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  
  imgray      = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  ret, thresh = cv2.threshold(imgray, 127, 255, 0)
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

  cv2.drawContours(frame, contours, -1, (0,255,0), 3)

  cv2.imshow('White Board', frame)

  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
