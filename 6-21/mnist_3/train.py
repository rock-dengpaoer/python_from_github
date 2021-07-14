import os
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

'''
python 3.7
tensorflow 2.0.0b0
'''


class CNN(object):
    def __init__(self):
        # Keras Sequential 顺序模型
        # 顺序模型是多个网络层的线性堆迭

        model = models.Sequential()

        # 第1层卷积，卷积核大小为3*3，32个，28*28为待训练图片的大小
        # 第一个参数，函数的位置参数filters，位置是固定的，含义是滤波器的个数，即卷积核的个数
        # 第二个参数，位置固定，卷积核的大小
        # activation 激活函数，为relu
        # input_shape   输入的形状
        # 关键字参数strides=(1, 1)，滑动步长，默认横向和纵向滑动均为1
        model.add(layers.Conv2D(
            32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

        # 池化层 最大池化层，取最大值
        # （2，2）会把输入张量的两个维度都缩小一半。 如果只使用一个整数，那么两个维度都会使用同样的窗口长度。
        model.add(layers.MaxPooling2D((2, 2)))

        # 第2层卷积，卷积核大小为3*3，64个
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))

        # 池化层
        model.add(layers.MaxPooling2D((2, 2)))

        # 第3层卷积，卷积核大小为3*3，64个
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))

        # 将三维张量展开为一维
        model.add(layers.Flatten())

        # 添加 Dense层
        # 等同于全连接层
        # Dense 层的输入为向量（一维），但前面层的输出是3维的张量 (Tensor)。
        # 因此您需要将三维张量展开 (flatten) 到1维，之后再传入一个或多个 Dense 层。
        # MNIST 数据集有 10 个类，因此您最终的 Dense 层需要 10 个输出及一个 softmax 激活函数。
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))

        # 查看完整的 CNN 结构：
        model.summary()

        self.model = model


class DataSource(object):
    def __init__(self):
        # mnist数据集存储的位置，如何不存在将自动下载
        data_path = os.path.abspath(os.path.dirname(
            __file__)) + '/../data_set_tf2/mnist.npz'

        #
        (train_images, train_labels), (test_images,
                                       test_labels) = datasets.mnist.load_data(path=data_path)

        # 6万张训练图片，1万张测试图片
        train_images = train_images.reshape((60000, 28, 28, 1))
        test_images = test_images.reshape((10000, 28, 28, 1))

        # 像素值映射到 0 - 1 之间
        train_images, test_images = train_images / 255.0, test_images / 255.0

        self.train_images, self.train_labels = train_images, train_labels
        self.test_images, self.test_labels = test_images, test_labels


class Train:
    def __init__(self):
        self.cnn = CNN()
        self.data = DataSource()

    def train(self):
        check_path = './ckpt/cp-{epoch:04d}.ckpt'
        # period 每隔5epoch保存一次
        save_model_cb = tf.keras.callbacks.ModelCheckpoint(
            check_path, save_weights_only=True, verbose=1, period=5)

        # 编译模型
        self.cnn.model.compile(optimizer='adam',
                               loss='sparse_categorical_crossentropy',
                               metrics=['accuracy'])

        # 训练模型
        self.cnn.model.fit(self.data.train_images, self.data.train_labels,
                           epochs=5, callbacks=[save_model_cb])

        test_loss, test_acc = self.cnn.model.evaluate(
            self.data.test_images, self.data.test_labels)
        print("准确率: %.4f，共测试了%d张图片 " % (test_acc, len(self.data.test_labels)))


if __name__ == "__main__":
    app = Train()
    app.train()
