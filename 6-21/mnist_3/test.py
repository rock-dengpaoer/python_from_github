import cv2 as cv
import numpy as np


def create_image():
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.zeros([400, 400]) + 255
    img[:, :, 1] = np.ones([400, 400]) + 254
    img[:, :, 2] = np.ones([400, 400]) * 255
    cv.imshow("iamge", img)
    img2 = np.zeros([400, 400, 3], np.uint8) + 255
    cv.imshow("iamge2", img2)
    cv.waitKey(0)

if __name__ =='__main__':
    create_image()

