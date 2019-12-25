import cv2 as cv, numpy as np, random

img = cv.imread("/home/junsoofeb/py_project/OpenCV/lena.jpg") 
w, h = img.shape[0], img.shape[1]

copy = img.copy()

moues_pressed = False
s_x = s_y  = e_x = e_y = -1


def mouse_callback(event, x, y, flags, param):
    global img, copy, s_x, s_y, e_x, e_y, moues_pressed
    
    if event == cv.EVENT_LBUTTONDOWN:
        moues_pressed = True
        s_x, s_y = x, y
        img = img.copy()
    
    elif event == cv.EVENT_MOUSEMOVE:
        if moues_pressed:
            copy = img.copy()
            cv.rectangle(copy, (s_x, s_y), (x, y), (0, 255, 0), 1)

    elif event == cv.EVENT_LBUTTONUP:
        moues_pressed = False
        e_x, e_y = x, y

cv.namedWindow("image")
cv.setMouseCallback('image', mouse_callback)    

print("Press 'c' to cut image!")

while True:
    cv.imshow('image', copy)
    key = cv.waitKey(1)
    
    if key == ord('c'):
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        if s_x > e_x:
            s_x , e_x = e_x, s_x
            
        if e_y - s_y > 1 and e_x - s_x > 0:
            img = img[s_y:e_y , s_x:e_x]
            copy = img.copy()
    
    elif key == 27:
        break
    
cv.destroyAllWindows()