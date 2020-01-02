import cv2 as cv, numpy as np, matplotlib.pyplot as plt

def show(image):
    cv.imshow("", image)
    cv.waitKey()
    cv.destroyAllWindows()

img = cv.imread("./OpenCV/lena.jpg", 0)

img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)[1]  # ensure binary
ret, labels = cv.connectedComponents(img)

def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv.cvtColor(labeled_img, cv.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue==0] = 0

    cv.imshow('labeled.png', labeled_img)
    cv.waitKey()

imshow_components(labels)