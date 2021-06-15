import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("1.jpg"))
# 将图像文件转换为矩阵
# print(img)
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
# 显示mat对象
k = cv.waitKey(0)
# 按键等待，0为一直等待
if k == ord("s"):
    # 如果按键为s
    cv.imwrite("starry_night.png", img)
    # 将矩阵写入图像文件
