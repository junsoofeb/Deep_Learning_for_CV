import cv2 as cv, numpy as np, matplotlib.pyplot as plt
from random import randint

# 숫자키 누르고 마우스 좌클릭! ex) 0누르고 좌클릭 -> 1누르고 좌클릭 -> ...

def show(image):
    cv.imshow("", image)
    cv.waitKey()
    cv.destroyAllWindows()


img = cv.imread("./OpenCV/lena.jpg")
show_img = np.copy(img)

seeds = np.full(img.shape[0:2], 0, np.int32)
segmentation = np.full(img.shape, 0, np.uint8)

n_seeds = 9

colors = []
for m in range(n_seeds):
    colors.append((255 * m / n_seeds, randint(0, 255), randint(0, 255)))

mouse_pressed = False
current_seed = 1
seeds_updated = False


def mouse_callback(event, x, y, flags, param):
    global mouse_pressed, seeds_updated

    if event == cv.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        cv.circle(seeds, (x, y), 5, (current_seed), cv.FILLED)
        cv.circle(show_img, (x, y), 5, colors[current_seed - 1], cv.FILLED)
        seeds_updated = True

    elif event == cv.EVENT_MOUSEMOVE:
        if mouse_pressed:
            cv.circle(seeds, (x, y), 5, (current_seed), cv.FILLED)
            cv.circle(show_img, (x, y), 5, colors[current_seed - 1], cv.FILLED)
            seeds_updated = True

    elif event == cv.EVENT_LBUTTONUP:
        mouse_pressed = False

cv.namedWindow('image')
cv.setMouseCallback('image', mouse_callback)



while True:
    cv.imshow('segmentation', segmentation)
    cv.imshow('image', show_img)
        
    k = cv.waitKey(1)

    if k == 27:
        break
    
    elif k == ord('c'):
        show_img = np.copy(img)
        seeds = np.full(img.shape[0:2], 0, np.int32)
        segmentation = np.full(img.shape, 0, np.uint8)
        
    elif k > 0 and chr(k).isdigit():
        n = int(chr(k))
        if 1 <= n <= n_seeds and not mouse_pressed:
            current_seed = n
    
    if seeds_updated and not mouse_pressed:        
        seeds_copy = np.copy(seeds)
        cv.watershed(img, seeds_copy)
        segmentation = np.full(img.shape, 0, np.uint8)
        for m in range(n_seeds):
            segmentation[seeds_copy == (m + 1)] = colors[m]
        
        seeds_updated = False
        
cv.destroyAllWindows()