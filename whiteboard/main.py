import numpy as np
import cv2

def getNewPoints(mask, color):
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  for c in contours:
    area = cv2.contourArea(c)

    if area > 3000:
      M = cv2.moments(c)
      if (M["m00"] == 0): M["m00"] == 1
      x = int(M["m10"]/M["m00"])
      y = int(M["m01"]/M["m00"])

      cv2.circle(whiteboard, (x, y), 5, color, -1)
      font = cv2.FONT_HERSHEY_SIMPLEX
      print('{},{} Areas: {}'.format(x, y, area))

      cv2.putText(frame, '{},{} Areas: {}'.format(x, y, area), (x+10, y), font, 0.75, color, 1, cv2.LINE_AA)


def create_whiteboard(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image

cap = cv2.VideoCapture(0)

lower_red_1 = np.array([0, 100, 20])
upper_red_1 = np.array([5, 255, 255])

lower_red_2 = np.array([175, 100, 20])
upper_red_2 = np.array([180, 255, 255])

lower_blue = np.array([118, 100, 20])
upper_blue = np.array([125, 255, 255])

lower_yellow = np.array([25, 100, 20])
upper_yellow = np.array([35, 255, 255])

whiteboard = None

while True:
  ret, frame = cap.read()

  if whiteboard is None:
    whiteboard = create_whiteboard(frame.shape[1], frame.shape[0])

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # mask_red_low = cv2.inRange(hsv, lower_red_1, upper_red_1)
  mask_red_upper = cv2.inRange(hsv, lower_red_2, upper_red_2)
  # red_mask = cv2.add(mask_red_low, mask_red_upper)

  red_mask = cv2.inRange(hsv, lower_red_2, upper_red_2)
  blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
  yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

  getNewPoints(blue_mask, (255,0 , 0))
  getNewPoints(yellow_mask, (0, 255, 255))
  getNewPoints(red_mask, (0, 0, 255))

  # maskRedVis = cv2.bitwise_and(frame, frame, mask=mask)

  full = cv2.add(frame, whiteboard)
  cv2.imshow('White Board', full)

  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
