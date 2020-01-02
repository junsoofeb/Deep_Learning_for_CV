
import cv2 as cv
import numpy as np


img = cv.imread('./OpenCV/lena.jpg', 0)

connectivity = 8
num_labels, labelmap = cv.connectedComponents(img, connectivity, cv.CV_32S)
img = np.hstack((img, labelmap.astype(np.float32)/(num_labels - 1)))

cv.imshow('Connected components', img)
cv.waitKey()
cv.destroyAllWindows()

img = cv.imread('./OpenCV/lena.jpg', 0)
_, otsu_mask = cv.threshold(img, -1, 1, cv.THRESH_BINARY | cv.THRESH_OTSU)

output = cv.connectedComponentsWithStats(otsu_mask, connectivity, cv.CV_32S)

num_labels, labelmap, stats, centers = output

colored = np.full((img.shape[0], img.shape[1], 3), 0, np.uint8)

for i in range(1, num_labels):
    if stats[i][4] > 200:
        colored[labelmap == i] = (0, 255*i/num_labels, 255*num_labels/i)
        cv.circle(colored, (int(centers[i][0]), int(centers[i][1])), 5, (255, 0, 0), cv.FILLED)
        
img = cv.cvtColor(otsu_mask*255, cv.COLOR_GRAY2BGR)

cv.imshow('Connected components', np.hstack((img, colored)))
cv.waitKey()
cv.destroyAllWindows()
