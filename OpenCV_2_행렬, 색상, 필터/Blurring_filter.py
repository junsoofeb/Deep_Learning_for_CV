import cv2 as cv, numpy as np
import matplotlib.pyplot as plt

def show(image):
    cv.imshow("", image)
    cv.waitKey()
    cv.destroyAllWindows()

# 이미지를 [0,1] 범위의 실수형 데이터 타입으로 변환
img = cv.imread("./OpenCV/lena.jpg").astype(np.float32) / 255

noise = (img + 0.2 * np.random.rand(*img.shape).astype(np.float32))
noise = noise.clip(0, 1)
show(noise)

gaussian = cv.GaussianBlur(noise, (3, 3), 0)
show(gaussian)

median = cv.medianBlur(noise, 5)
show(median)

bilateral = cv.bilateralFilter(noise, 5, 50, 50)
show(bilateral)