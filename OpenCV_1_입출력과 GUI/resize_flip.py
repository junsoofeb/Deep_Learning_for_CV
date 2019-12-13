import cv2 as cv

def show(frame):
    cv.imshow("", frame)
    cv.waitKey()
    cv.destroyAllWindows()


img = cv.imread("C:/Users/kwon/Desktop/lena.png")

test = img.copy()


# 이미지 크기 조절
# img = cv.resize(input, (width, height))
img = cv.resize(img, (200,200))
show(img)


# 이미지 뒤집기  
# 마지막 인자가 0이면 x축을 따라 뒤집고, 1이면 y축을 따라 뒤집는다
# 마지막 인자가 음수면 x, y 축을 동시에 뒤집는다.
img = cv.flip(test , 0)
show(img) 

img = cv.flip(test , 1) 
show(img) 

img = cv.flip(test , -1) 
show(img) 