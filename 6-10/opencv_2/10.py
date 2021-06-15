import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

img1 = cv.imread('opencv.png')

replicate = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
# 如果要在图像周围创建边框，例如相框，可以使用cv.copyMakeBorder()。但它在卷积运算、零填充等方面有更多应用。该函数采用以下参数：
#
# src - 输入图像
# 上、下、左、右边框宽度（以相应方向的像素数表示）
# borderType - 定义要添加的边框类型的标志。它可以是以下类型：
# cv.BORDER_CONSTANT - 添加一个恒定的彩色边框。该值应作为下一个参数给出。
# cv.BORDER_REFLECT - 边框将是边框元素的镜像，像这样： fedcba|abcdefgh|hgfedcb
# cv.BORDER_REFLECT_101或cv.BORDER_DEFAULT - 与上面相同，但略有变化，如下所示： gfedcb|abcdefgh|gfedcba
# cv.BORDER_REPLICATE - 最后一个元素被复制，像这样： aaaaaa|abcdefgh|hhhhhhh
# cv.BORDER_WRAP - 无法解释，它看起来像这样： cdefgh|abcdefgh|abcdefg
# value - 如果边框类型为cv.BORDER_CONSTANT的边框颜色