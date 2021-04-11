import cv2 as cv

# Reading IMG
img = cv.imread('photos/cat1.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)

  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Cat Re', resized_image)

# press 0 to exit
cv.waitKey(0)

# Reading Videos
if False:
  capture = cv.VideoCapture(0)
  while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
      break

  capture.release()
  cv.destroyAllWindows()

