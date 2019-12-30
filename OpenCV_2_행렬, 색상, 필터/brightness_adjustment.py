import cv2 as cv, numpy as np

# gamma > 1 ====> 이미지가 어두워지도록 할 때!
# gamma < 1 ====> 이미지가 밝아지도록 할 때!

img = cv.imread("/home/junsoofeb/py_project/OpenCV/lena.jpg").astype(np.float32) / 255

cv.imshow("oringinal img", img)
cv.waitKey()
cv.destroyAllWindows()

gamma = 0.5

changed_img = np.power(img, gamma)
cv.imshow("changed img", changed_img)
cv.waitKey()
cv.destroyAllWindows()


