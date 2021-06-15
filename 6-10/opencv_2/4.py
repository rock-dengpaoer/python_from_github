import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
# FourCC是用于指定视频编解码器的 4 字节代码
# 更多信息在https://www.fourcc.org/codecs.php
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?).Exiting ...")
        break
    # frame = cv.flip(frame, 0)
    # 图像上下翻转

    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
out.release()
cv.destroyAllWindows()