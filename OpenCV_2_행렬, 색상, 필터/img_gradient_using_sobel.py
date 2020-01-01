import cv2 as cv, numpy as np, matplotlib.pyplot as plt

def show(image):
    cv.imshow("", image)
    cv.waitKey()
    cv.destroyAllWindows()
    
img = cv.imread("./OpenCV/lena.jpg", 0)

dx = cv.Sobel(img, cv.CV_32F, 1, 0)
dy = cv.Sobel(img, cv.CV_32F, 0, 1)

show(dx)
show(dy)

plt.figure(figsize=(8, 3))

plt.subplot(131)
plt.axis('off')
plt.title('image')
plt.imshow(img, cmap = 'gray')

plt.subplot(132)
plt.axis('off')
plt.imshow(dx, cmap = 'gray')
plt.title('dI/dx')

plt.subplot(133)
plt.axis('off')
plt.imshow(dy, cmap = 'gray')
plt.title('dI/dy')

plt.tight_layout()
plt.show()