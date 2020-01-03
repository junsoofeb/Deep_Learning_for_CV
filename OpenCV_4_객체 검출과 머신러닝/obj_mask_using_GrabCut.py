import cv2 as cv, numpy as np, matplotlib.pyplot as plt
from random import randint

# 마우스오 사각형 그리고 a눌러서 사용!

img = cv.imread("./OpenCV/lena.jpg")
show_img = np.copy(img)

mouse_pressed = False
y = x = w = h = 0

def mouse_callback(event, _x, _y, flags, param):
    global show_img, x, y, w, h, mouse_pressed

    if event == cv.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        x, y = _x, _y
        show_img = np.copy(img)

    elif event == cv.EVENT_MOUSEMOVE:
        if mouse_pressed:
            show_img = np.copy(img)
            cv.rectangle(show_img, (x, y), (_x, _y), (0, 255, 0), 3)

    elif event == cv.EVENT_LBUTTONUP:
        mouse_pressed = False
        w, h = _x - x, _y - y
        
cv.namedWindow('image')
cv.setMouseCallback('image', mouse_callback)

while True:
    cv.imshow('image', show_img)
    k = cv.waitKey(1)

    if k == ord('a') and not mouse_pressed:
        if w*h > 0:
            break

cv.destroyAllWindows()


labels = np.zeros(img.shape[:2],np.uint8)

labels, bgdModel, fgdModel = cv.grabCut(img, labels, (x, y, w, h), None, None, 5, cv.GC_INIT_WITH_RECT)

show_img = np.copy(img)
show_img[(labels == cv.GC_PR_BGD)|(labels == cv.GC_BGD)] //= 3

cv.imshow('image', show_img)
cv.waitKey()
cv.destroyAllWindows()

label = cv.GC_BGD
lbl_clrs = {cv.GC_BGD: (0,0,0), cv.GC_FGD: (255,255,255)}

def mouse_callback(event, x, y, flags, param):
    global mouse_pressed

    if event == cv.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        cv.circle(labels, (x, y), 5, label, cv.FILLED)
        cv.circle(show_img, (x, y), 5, lbl_clrs[label], cv.FILLED)

    elif event == cv.EVENT_MOUSEMOVE:
        if mouse_pressed:
            cv.circle(labels, (x, y), 5, label, cv.FILLED)
            cv.circle(show_img, (x, y), 5, lbl_clrs[label], cv.FILLED)

    elif event == cv.EVENT_LBUTTONUP:
        mouse_pressed = False
        
cv.namedWindow('image')
cv.setMouseCallback('image', mouse_callback)

while True:
    cv.imshow('image', show_img)
    k = cv.waitKey(1)

    if k == ord('a') and not mouse_pressed:
        break
    elif k == ord('l'):
        label = cv.GC_FGD - label

cv.destroyAllWindows()

labels, bgdModel, fgdModel = cv.grabCut(img, labels, None, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_MASK)

show_img = np.copy(img)
show_img[(labels == cv.GC_PR_BGD)|(labels == cv.GC_BGD)] //= 3

cv.imshow('image', show_img)
cv.waitKey()
cv.destroyAllWindows()