import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)
# 创建一个黑色图像

cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 画一条直线
# (0, 0), (511, 511)代表起点和终点
# (255, 0, 0)代表蓝色
# 5 代表厚度
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# 绘制矩形
# (384, 0), (510, 128) 左上角和右下角的坐标
# (0, 255, 0) 颜色 绿
# 3 厚度
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
# 画圆
# (447, 63), 63)　圆心坐标，半径
# (0, 0, 255)　颜色
# -1 厚度，-1代表为填充
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# 画椭圆，这是个半椭圆
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))
# 画多边形
# 首先给出顶点坐标
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OPENCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)
# 写字
cv.imshow("Display window", img)
# 显示图像
k = cv.waitKey(0)
