import cv2 as cv
import numpy as np, sys

# 合成图像

# 加载苹果和橙子的两张图片
# 找到苹果和橙子的高斯金字塔（在这个特定的例子中，层数是 6）
# 从高斯金字塔，找到他们的拉普拉斯金字塔
# 现在在拉普拉斯金字塔的每一层加入左半边的苹果和右半边的橙子
# 最后从这个联合图像金字塔，重建原始图像。

A = cv.imread('apple.jpg')
B = cv.imread('orange.jpg')

# 高斯金字塔
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)
# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# 拉普拉斯金字塔
# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i - 1], GE)
    lpA.append(L)
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i - 1], GE)
    lpB.append(L)
# Now add left and right halves of images in each level
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols // 2], lb[:, cols // 2:]))
    #  ls = np.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
    # 报错
    # slice indices must be integers or None or have an __index__ method
    # 原因， 经过/运算后，变成浮点类型数据。
    # 更改 // 	取整除 - 返回商的整数部分（向下取整） 解决问题
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])
# image with direct connecting each half
real = np.hstack((A[:, :cols // 2], B[:, cols // 2:]))
cv.imwrite('Pyramid_blending2.jpg', ls_)
cv.imwrite('Direct_blending.jpg', real)
