import numpy as np
import cv2

cap = cv2.VideoCapture(0)

lower_red_1 = np.array([0, 100, 20])
upper_red_1 = np.array([8, 255, 255])

lower_red_2 = np.array([175, 100, 20])
upper_red_2 = np.array([179, 255, 255])

lower_blue = np.array([100, 100, 20])
upper_blue = np.array([125, 255, 255])

while True:
  ret, frame = cap.read()
  hsv   = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
  # mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
  # mask3 = cv2.inRange(hsv, lower_blue, upper_blue)
  mask = cv2.inRange(hsv, lower_blue, upper_blue)

  #mask = cv2.add(mask1, mask2)
  #mask = cv2.add(mask, mask3)

  contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  for c in contours:
    area = cv2.contourArea(c)

    if area > 3000:
      M = cv2.moments(c)
      if (M["m00"] == 0): M["m00"] == 1
      x = int(M["m10"]/M["m00"])
      y = int(M["m01"]/M["m00"])
  
      cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
      font = cv2.FONT_HERSHEY_SIMPLEX
      cv2.putText(frame, '{},{}'.format(x, y), (x+10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)

      newContours = cv2.convexHull(c)
      cv2.drawContours(frame, [newContours], 0, (255, 0, 0), 3)

  # maskRedVis = cv2.bitwise_and(frame, frame, mask=mask)

  cv2.imshow('White Board', frame)

  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
