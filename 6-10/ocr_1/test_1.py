import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('1.jpg', 0)
res = cv.resize(img, None, fx=0.1, fy=0.1, interpolation=cv.INTER_LINEAR)

cv.imshow('image', res)
k = cv.waitKey(0)