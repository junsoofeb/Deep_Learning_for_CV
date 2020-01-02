import cv2 as cv
import numpy as np
import random


def show(string, image):
    cv.imshow(string, image)
    cv.waitKey()
    cv.destroyAllWindows()    

img = np.full((512, 512, 3), 255, np.uint8)

axes = (int(256*random.uniform(0, 1)), int(256*random.uniform(0, 1)))
angle = int(180*random.uniform(0, 1))
center = (256, 256)


pts = cv.ellipse2Poly(center, axes, angle, 0, 360, 1)
pts += np.random.uniform(-10, 10, pts.shape).astype(np.int32)

cv.ellipse(img, center, axes, angle, 0, 360, (0, 255, 0), 3)

for pt in pts:
    cv.circle(img, (int(pt[0]), int(pt[1])), 3, (0, 0, 255))

show('fit ellipse', img)

ellipse = cv.fitEllipse(pts)
cv.ellipse(img, ellipse, (0, 0, 0), 3)

show('fit ellipse', img)

img = np.full((512, 512, 3), 255, np.uint8)

pts = np.arange(512).reshape(-1, 1)
pts = np.hstack((pts, pts))
pts += np.random.uniform(-10, 10, pts.shape).astype(np.int32)

cv.line(img, (0,0), (512, 512), (0, 255, 0), 3)

for pt in pts:
    cv.circle(img, (int(pt[0]), int(pt[1])), 3, (0, 0, 255))

show("fit_line", img)

vx,vy,x,y = cv.fitLine(pts, cv.DIST_L2, 0, 0.01, 0.01)
y0 = int(y - x*vy/vx)
y1 = int((512 - x)*vy/vx + y)
cv.line(img, (0, y0), (512, y1), (0, 0, 0), 3)

show("fit_line", img)
