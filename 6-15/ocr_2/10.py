# 为了获得更好的准确性，请使用二进制图像。所以在找到轮廓之前，应用阈值或精明的边缘检测。
# 从 OpenCV 3.2 开始，findContours()不再修改源图像。
# 在 OpenCV 中，寻找轮廓就像从黑色背景中寻找白色物体。所以请记住，要找到的对象应该是白色的，背景应该是黑色的。

import numpy as np
import cv2 as cv
im = cv.imread('test-5.png')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.imshow('image', imgray)
cv.waitKey(0)
