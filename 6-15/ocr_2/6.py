from random import random

import cv2 as cv
import numpy as np

img = cv.imread('test-5.png', 0)
kernel = np.ones((20, 20), np.uint8)
# 自动创建的内核

# 手动创建内核
# kernel_rect = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# 矩阵内核
# print(kernel_rect)

# kernel_ELLIPSE = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
# 椭圆内核
# print(kernel_ELLIPSE)

kernel_CROSS = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
# 十字内核
print(kernel_CROSS)

# 还有其他内核形状，本质是一个数组array，也可以自己创建


# erosion = cv.erode(img, kernel, iterations=1)
# 侵蚀
# cv.imshow('images', erosion)

# dilation = cv.dilate(img, kernel, iterations=1)
# 膨胀
# cv.imshow('images', dilation)


def sp_noise(image, prob):
    """
    添加椒盐噪声
    prob:噪声比例
    """
    output = np.zeros(image.shape, np.uint8)
    threes = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > threes:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


# cv.imshow('images', img)

# img = sp_noise(img, 0.01)
# cv.imshow('images-1', img)

# opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
# 开幕
# cv.imshow('images', opening)

# closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
# 关幕
# cv.imshow('images', closing)

# gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
# 形态梯度
# cv.imshow('images', gradient)

# tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
# 礼帽 top hat
# cv.imshow('images', tophat)

# blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
# 黑帽 black hat
# cv.imshow('images', blackhat)


cv.waitKey(0)
