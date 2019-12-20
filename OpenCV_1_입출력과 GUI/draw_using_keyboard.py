import cv2 as cv, numpy as np, random

img = cv.imread("/home/junsoofeb/py_project/OpenCV/lena.jpg") 
w, h = img.shape[0], img.shape[1]


def show(image):
    cv.imshow("", image)
    key = cv.waitKey()
    cv.destroyAllWindows()
    return key

def random_point():
    return (random.randrange(w), random.randrange(h))


while True:
    key = show(img)
    if key == ord('c'):
        print("Draw_Circle_random_position!")
        for pt in [random_point() for _ in range(5)]:
            cv.circle(img, pt, 5, (255, 0, 0), -1)
    elif key == ord('t'):
        print("Draw_Text_random_position!")
        cv.putText(img, 'STUDY', random_point(), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)    
    elif key == ord('r'):
        print("Draw_Rectangle_random_position!")
        cv.rectangle(img, random_point(), random_point(), (0, 0, 255),2)
    elif key == ord('e'):
        print("Erase all!")
        img = cv.imread("/home/junsoofeb/py_project/OpenCV/lena.jpg") 
    elif key == 27: # esc
        break