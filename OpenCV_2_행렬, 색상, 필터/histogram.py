import cv2 as cv, numpy as np
import matplotlib.pyplot as plt

gray_img = cv.imread("./OpenCV/lena.jpg", 0)
cv.imshow("gray img", gray_img)
cv.waitKey()
cv.destroyAllWindows()

# matplot 사용
plt.hist (gray_img.ravel (), 256, [0,256])
plt.show ()

# opencv 내장함수 사용
'''
cv.calcHist (이미지, 채널, 마스크, histSize, 범위 [, hist [, 누적]])

1. images : uint8 또는 float32 이미지, [img]처럼 대괄호로 묶어야 함
2. 채널 : [0]처럼 대괄호로 줘야함. 회색조 = [0], 컬러 이미지는 [0], [1], [2] 각각 B, G, R 순서
3. 마스크 :  None을 줘야 전체이미지의 히스토그램
4. histSize : Bin의 개수, 대괄호로 줘야함, [256]이 최대
5. 범위 : 보통 [0, 256]
'''
hist = cv.calcHist([gray_img],[0],None,[256],[0,256])

# numpy 사용
hist, bins = np.histogram(gray_img, 256, [0, 255])

plt.fill(hist)
plt.xlabel('pixel value')
plt.show()