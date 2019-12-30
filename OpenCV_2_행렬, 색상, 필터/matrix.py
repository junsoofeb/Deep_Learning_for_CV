import cv2 as cv, numpy as np

# np.full((h,w,c), 초깃값, 데이터타입)
img = np.full((480, 640, 3), 255, np.uint8) # 흰색 이미지 생성 
#img = np.full((480, 640, 3), 0, np.uint8) # 검은색 이미지 생성 
# img.fill(0) 도 검은색 이미지 생성!

cv.imshow("white img", img)
cv.waitKey()
cv.destroyAllWindows()

img = np.full((480, 640, 3), (0, 0, 255), np.uint8) # BGR채널 중 R채널을 255로 채움 -> 빨간 이미지 생성
cv.imshow("red img", img)
cv.waitKey()
cv.destroyAllWindows()

img.fill(0)

img[:, :, 0] = 255
cv.imshow("blue img", img)
cv.waitKey()
cv.destroyAllWindows()

