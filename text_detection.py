import cv2 as cv

def show(frame):
    cv.imshow("", frame)
    cv.waitKey()
    cv.destroyAllWindows()

def area(rect):
    w = rect[2] 
    h = rect[3]
    
    return w * h

def main():
    img = None
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 500) # cap.set(3, 500)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 500) # cap.set(4, 500)
    while 1:
        ret, frame = cap.read()
        cv.imshow("web cam",frame)
        k = cv.waitKey(1)
        if k == 27: # esc 누르면 종료
            img = frame.copy()
            break
    cap.release()

    det = cv.text.TextDetectorCNN_create("./textbox.prototxt", "./TextBoxes_icdar13.caffemodel")
    rects, probs = det.detect(img)
    

    THR = 0.01
    for i, r in enumerate(rects):
        if probs[i] > THR and area(rects[i]) < 3000:
            cv.rectangle(img, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), (0, 255, 0), 2)
                                    # 좌상단     # 우하단

    THR = 0.3
    for i, r in enumerate(rects):
        if probs[i] > THR :
            cv.rectangle(img, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), (255, 0, 0), 2)

    show(img)


while 1:
    main()