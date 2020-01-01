import cv2 as cv, numpy as np, matplotlib.pyplot as plt

def show(image):
    cv.imshow("", image)
    cv.waitKey()
    cv.destroyAllWindows()

img = cv.imread("./OpenCV/lena.jpg")

internal = img.copy()
external = img.copy()
c = img.copy()

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
show(img)

ret, thresh = cv.threshold(img, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)


# 윤곽선
for cnt in range(len(contours)):
    cv.drawContours(c, contours, cnt, (255, 0, 0))
    
show(c)

'''
# 외부
for cnt in range(len(contours)):
    if hierarchy[0][cnt][3] == -1:
        cv.drawContours(external, contours, cnt, (0, 0, 255), -1)
# 내부    
for cnt in range(len(contours)):
    if hierarchy[0][cnt][3] != -1:
        cv.drawContours(internal, contours, cnt, (0, 255, 0), -1)
        
show(external)
show(internal)
'''