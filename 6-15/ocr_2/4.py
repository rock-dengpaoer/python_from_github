from random import random

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread('opencv-logo-white.png')

img = cv.imread('squirrel_cls.jpg')


def sp_noise(image, prob):
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


img = sp_noise(img, 0.1)

# blur = cv.blur(img, (5, 5))
# 平均模糊

# blur = cv.GaussianBlur(img, (5, 5), 0)
# 高斯模糊

# blur = cv.medianBlur(img, 5)
# 中值模糊

blur = cv.bilateralFilter(img, 9, 75, 75)
# 双边过滤


plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
