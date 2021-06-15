import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
print(cap)
if not cap.isOpened():
    # 检查cap是否已经初始化，已初始化返回True。若没有初始化，可以使用cap.Open()打开摄像头
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    # cap.read()返回一个布尔值，True/False。如果frame（框架）被读取，则返回True
    # print('ret=', ret)
    # print('frame=', frame)
    # cap.get(propld)访问视频的某些功能，propld值为0-18.
    # cv.CAP_PROP_FPS 帧率
    # print(cap.get(cv.CAP_PROP_FPS))
    # cv.CAP_PROP_POS_AVI_RATIO 视频文件的相对位置：0=影片开头，1=影片结尾。
    # print(cap.get(cv.CAP_PROP_POS_AVI_RATIO))
    # 具体细节在
    # https://docs.opencv.org/master/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    # VideoCaptureProperties分类
    # 其中一些值可以使用cap.set(propId, value)进行修改。值是您想要的新值。

    if not ret:
        print("Can't receive frame (stream end?).Exiting...")
        break

    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
    print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.COLOR_BGR2GRAY 颜色设置为灰度
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()