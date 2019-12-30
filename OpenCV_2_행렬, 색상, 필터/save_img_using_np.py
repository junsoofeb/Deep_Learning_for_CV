import cv2 as cv, numpy as np


# 이미지를 imwrite가 아닌 넘파이 형태로 바로 저장!
# 채널이 1 또는 2개만 가능!

mat = cv.imread("/home/junsoofeb/py_project/OpenCV/lena.jpg", 0) 
cv.imshow("mat", mat)
cv.waitKey()
cv.destroyAllWindows()
print("shape:", mat.shape)
print("data type:", mat.dtype)

mat = np.savetxt('mat.csv', mat)

mat = np.loadtxt('mat.csv').astype(np.uint8)
mat = cv.Canny(mat, 50, 100)
cv.imshow("canny", mat)
cv.waitKey()
cv.destroyAllWindows()