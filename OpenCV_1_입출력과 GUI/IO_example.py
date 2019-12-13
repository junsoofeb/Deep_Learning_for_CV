import cv2 as cv

def show(frame):
    cv.imshow("", frame)
    cv.waitKey()
    cv.destroyAllWindows()

# 파일에서 이미지 읽어오기 
# cv.imread(file path [, flag])
# 이미지 출력
# cv.imshow(window_name, img)
img = cv.imread("C:/Users/kwon/Desktop/lena.png")
show(img)

'''
# flag를 0으로 주면 grayscale
img = cv.imread("C:/Users/kwon/Desktop/lena.png", 0)
show(img)

# flag 
# 16 >> 1/2 사이즈의 grayscale 이미지  17 >> 1/2 사이즈의 BGR 3 채널 이미지 
# 32 >> 1/4 사이즈의 grayscale 이미지  33 >> 1/4 사이즈의 BGR 3 채널 이미지 
# 64 >> 1/8 사이즈의 grayscale 이미지  65 >> 1/8 사이즈의 BGR 3 채널 이미지 

img = cv.imread("C:/Users/kwon/Desktop/lena.png", 16)
show(img)

img = cv.imread("C:/Users/kwon/Desktop/lena.png", 17)
show(img)
'''

# 파일에서 읽어온 이미지는 넘파이 배열이다.
# default dtype은 uint8

shape = img.shape
dtype = img.dtype

print(f"shape : {shape}")
print(f"dtype : {dtype}")


