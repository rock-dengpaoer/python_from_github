import tensorflow as tf
from PIL import Image
import numpy as np
import cv2 as cv

from train import CNN

'''
python 3.7
tensorflow 2.0.0b0
pillow(PIL) 4.3.0
'''

drawing = False


class Predict(object):
    def __init__(self):
        latest = tf.train.latest_checkpoint('./ckpt')
        self.cnn = CNN()
        # 恢复网络权重
        self.cnn.model.load_weights(latest)

    # def predict(self, image_path):
    #     # 以黑白方式读取图片
    #     img = Image.open(image_path).convert('L')
    #     img = np.reshape(img, (28, 28, 1)) / 255.
    #     x = np.array([1 - img])
    #
    #     # API refer: https://keras.io/models/model/
    #     y = self.cnn.model.predict(x)
    #
    #     # 因为x只传入了一张图片，取y[0]即可
    #     # np.argmax()取得最大值的下标，即代表的数字
    #     print(image_path)
    #     print(y[0])
    #     print('        -> Predict digit', np.argmax(y[0]))

    def predict(self, image_path):
        # 以黑白方式读取图片
        img = Image.open(image_path).convert('L')
        img = np.reshape(img, (28, 28, 1)) / 255.
        x = np.array([1 - img])

        # API refer: https://keras.io/models/model/
        y = self.cnn.model.predict(x)

        # 因为x只传入了一张图片，取y[0]即可
        # np.argmax()取得最大值的下标，即代表的数字
        print(image_path)
        print(y[0])
        print('        -> Predict digit', np.argmax(y[0]))


def nothing(x):
    pass


def draw(event, x, y, flags, param):
    global drawing
    if event == cv.EVENT_LBUTTONDOWN:  # 响应鼠标按下
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:  # 响应鼠标移动
        if drawing:
            img[y:y + 20, x:x + 20] = (0, 0, 0)
    elif event == cv.EVENT_LBUTTONUP:  # 响应鼠标松开
        drawing = False


if __name__ == "__main__":
    app = Predict()
    # app.predict('../test_images/0.png')
    # app.predict('../test_images/1.png')
    # app.predict('../test_images/4.png')
    # 创建一个白色的图像，一个窗口
    img = np.zeros((300, 300, 3), np.uint8)+255

    cv.namedWindow('image')

    clear = 'clear'
    distinguish = 'distinguish'

    cv.createTrackbar(distinguish, 'image', 0, 1, nothing)  # 识别数字
    cv.createTrackbar(clear, 'image', 0, 1, nothing)  # 清空画布

    cv.setMouseCallback('image', draw)
    img[:] = (255, 255, 255)  # 将画板设为白色

    while 1:
        cv.imshow('image', img)
        if cv.waitKey(1) & 0xFF == 27:
            break

        c = cv.getTrackbarPos(clear, 'image')
        d = cv.getTrackbarPos(distinguish, 'image')

        # 清空画布
        if c == 1:
            cv.setTrackbarPos(clear, 'image', 0)
            img[:] = (255, 255, 255)

        if d == 1:  # 识别数字
            # cv.setTrackbarPos(distinguish, 'image', 0)
            # testimg = img.copy()
            # testimg = cv.resize(testimg, (20, 20))
            # gray = cv.cvtColor(testimg, cv.COLOR_BGR2GRAY)
            # x = np.array(gray).reshape(-1, 400).astype(np.float32)
            # ret, result, neighbours, dist = knn.findNearest(x, k=5)
            # cv.putText(img, str(result[0][0]), (5, 25), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (100, 200, 200), 1)
            cv.setTrackbarPos(distinguish, 'image', 0)
            cv_img = img.copy()
            cv_img = cv.resize(cv_img, (28, 28))
            cv.imwrite("test.png", cv_img)
            app.predict('test.png')

    cv.destroyAllWindows()
