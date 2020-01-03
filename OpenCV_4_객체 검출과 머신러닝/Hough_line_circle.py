import cv2 as cv, numpy as np, matplotlib.pyplot as plt
from random import randint


def show(image, string = ""):
    cv.imshow(string, image)
    cv.waitKey()
    cv.destroyAllWindows()    

img = cv.imread("./OpenCV/lena.jpg", 0)
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 15, param1=200, param2=30)[0]
lines = cv.HoughLinesP(img, 1, np.pi/180, 100, 100, 10)[0]

dbg_img = cv.imread("./OpenCV/lena.jpg")
for x1, y1, x2, y2 in lines:
    cv.line(dbg_img, (x1, y1), (x2, y2), (255, 0, 0), 2)    

for c in circles:
    cv.circle(dbg_img, (c[0], c[1]), c[2], (0, 255, 0), 2)

show(dbg_img)