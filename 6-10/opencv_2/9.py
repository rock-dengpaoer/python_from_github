import numpy as np
import cv2 as cv

# img = cv.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
# 单通道读取图片

img = cv.imread('1.jpg')

# px = img[100, 100]
# print(px)
# 显示100,100像素点的rgb值

# blue = img[100, 100, 0]
# 0只显示蓝色色素的值, 1和-2显示绿色，2和-1显示红色
# print(blue)

# img[100, 100] = [255, 255, 255]
# 修改 特定像素点的颜色

# print(img[100, 100])
# cv.imshow('image', img)
# k = cv.waitKey(0)

# print(img[10, 10])
# print(img.item(10, 10, 2))
# 访问红色的值

# img.itemset((10, 10, 2), 100)
# print(img.item(10, 10, 2))
# 修改红色的值

# print(img.shape)
# 图像的属性，行数，列数，通道数的元祖（如果图像是彩色的）
# 如果图像是灰度的，则不显示通道数，由此判断是否为灰度；此方法以作废
# opencv在默认情况下会读取带有3个通道的图像，如果是灰度图/红外图片则会将其图层复制三次(RGB缺省)，因此读出来的图片是三通道。
# 如果我们想一开始就按照单通道读取灰度图片/红外图片的话，可以在imread()函数中加入相关参数(cv2.IMREAD_GRAYSCALE):

# print(img.size)
# 显示图像像素总数

# print(img.dtype)
# 图像数据类型

# nose = img[107:130, 106:120]
# img[107:130, 30:44] = nose
# ROI 感兴趣的地方， 复制该块区域
# 107:130，代表列数，起点到终点，106:120 代表行数

# b, g, r = cv.split(img)
# img = cv.merge((b, g, r))
# 拆分通道

# img[:, :, 2] = 0
# 将所有红色像素设置为零 - 您不需要先拆分通道。Numpy 索引更快
# cv.split()是一个代价高昂的操作（就时间而言）。所以只在必要时使用它。否则去 Numpy 索引。


cv.imshow('image', img)
k = cv.waitKey(0)
