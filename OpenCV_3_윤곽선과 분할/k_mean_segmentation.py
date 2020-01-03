import cv2 as cv, numpy as np
import matplotlib.pyplot as plt

def show(image):
    cv.imshow("", image)
    cv.waitKey()
    cv.destroyAllWindows()

# 이미지를 [0,1] 범위의 실수형 데이터 타입으로 변환
image = cv.imread("./OpenCV/lena.jpg").astype(np.float32) / 255
image_lab = cv.cvtColor(image, cv.COLOR_BGR2Lab)

# 이미지를 벡터형으로 변환
data = image_lab.reshape((-1, 3))

# 숫자 클수록 색이 다양
num_classes = 16
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 50, 0.1)
_, labels, centers = cv.kmeans(data, num_classes, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

segmented_lab = centers[labels.flatten()].reshape(image.shape)
segmented = cv.cvtColor(segmented_lab, cv.COLOR_Lab2BGR)

show(segmented)