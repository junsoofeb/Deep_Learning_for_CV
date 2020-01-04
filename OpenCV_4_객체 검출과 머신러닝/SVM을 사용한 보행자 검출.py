
import cv2
import numpy as np
import matplotlib.pyplot as plt

    
cap = cv2.VideoCapture(2)

#_, img = cap.read()

while True:
    status_cap, frame = cap.read()
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor.getDefaultPeopleDetector())
    locations, weights = hog.detectMultiScale(frame)
    dbg_image = frame.copy()
    for loc in locations:
        cv2.rectangle(dbg_image, (loc[0], loc[1]), (loc[0]+loc[2], loc[1]+loc[3]), (0, 255, 0), 2)

    cv2.imshow('svm', dbg_image)
    k = cv2.waitKey(1)
    if k == 27:
        break
    else:
        continue
cv2.destroyAllWindows()
