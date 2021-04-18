#pylint:disable=no-member

import numpy as np
import cv2 as cv

vid = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['steve_jobs', 'elon_musk', 'daniel_arenas']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

while (True):
  # Capture the video frame
  # by frame
  ret, frame = vid.read()
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  # Detect the face in the image
  faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

  for (x,y,w,h) in faces_rect:
      faces_roi = gray[y:y+h,x:x+w]

      label, confidence = face_recognizer.predict(faces_roi)
      print(f'Label = {people[label]} with a confidence of {confidence}')

      cv.putText(frame, str(people[label]), (x,y), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
      cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

  cv.imshow('Detected Face', frame)

  if cv.waitKey(0) & 0xFF == ord('q'):
      break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
