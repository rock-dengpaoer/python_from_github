import cv2 as cv
import numpy as np

drawing = False

# 一个创建鼠标作画的程序


def draw(event, x, y, flags, param):
    global drawing
    if event == cv.EVENT_LBUTTONDOWN:  # 响应鼠标按下
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:  # 响应鼠标移动
        if drawing:
            img[y:y + 20, x:x + 20] = (255, 255, 255)
    elif event == cv.EVENT_LBUTTONUP:  # 响应鼠标松开
        drawing = False


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw)

img[:] = (0, 0, 0)
while 1:
    cv.imshow('image', img)
    k = cv.waitKey(1)
    if k == ord('q'):
        cv.imwrite("test-5.png", img)
        break


