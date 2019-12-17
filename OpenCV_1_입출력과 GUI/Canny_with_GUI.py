import cv2 as cv
import numpy as np
import sys

fill_val = np.array([255, 255], np.uint8)

min = 50
max = 150


def trackbar_callback_min(min, im):
    global img
    img = cv.Canny(im, min, 100)

def trackbar_callback_max(max, im):
    global img
    img = cv.Canny(im, 100, max)
    
img = cv.imread("/home/junsoofeb/py_project/OpenCV/lena.jpg", 0) # grayscale
if img.size == 0:
    print("img load err!!")
    sys.exit()
        
cv.namedWindow("Lena and Canny edge!")
cv.createTrackbar("Min Val", "Lena and Canny edge!", 50, 255, lambda v: trackbar_callback_min(v, img))
cv.createTrackbar("Max Val", "Lena and Canny edge!", 150, 255, lambda v: trackbar_callback_max(v, img))

while True:
    cv.imshow("Lena and Canny edge!", img)
    key = cv.waitKey(3)
    if key == 27:
        break

cv.destroyAllWindows()