import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('1.jpg', 0)
res = cv.resize(img, None, fx=0.1, fy=0.1, interpolation=cv.INTER_LINEAR)

# cv.imshow('image', res)
# k = cv.waitKey(0)

img = cv.medianBlur(res, 5)

print(img.shape)

# res = np.zeros((20, 20, 3), np.uint8)

# res = cv.resize(img, None, fx=0.1, fy=0.1, interpolation=cv.INTER_LINEAR)
# 缩放十倍，比例不变
# print(res.shape)

ret, th1 = cv.threshold(img, 0, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,
            cv.THRESH_BINARY,11,2)
# th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY, 11, 2)

titles = ['original Image', 'Global Thresholding(v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# cv.imshow('image', res)
# cv.imshow('image', th3)
k = cv.waitKey(0)
