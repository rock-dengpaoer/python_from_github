# import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from model import Network
import tensorflow.compat.v1 as tf


tf.disable_v2_behavior()

CKPT_DIR = 'ckpt'


class Train:
    def __init__(self):
        self.net = Network()

        # 初始化 session
        # Network() 只是构造了一张计算图，计算需要放到会话(session)中
        self.sess = tf.Session()
        # 初始化变量
        self.sess.run(tf.global_variables_initializer())

        # 读取训练和测试数据，这是tensorflow库自带的，不存在训练集会自动下载
        # 项目目录下已经下载好，删掉后，重新运行代码会自动下载
        # data_set/train-images-idx3-ubyte.gz
        # data_set/train-labels-idx1-ubyte.gz
        # data_set/t10k-images-idx3-ubyte.gz
        # data_set/t10k-labels-idx1-ubyte.gz
        self.data = input_data.read_data_sets('../data_set', one_hot=True)

    # v1版本
    # def train(self):
    #     # batch_size 是指每次迭代训练，传入训练的图片张数。
    #     # 数据集小，可以使用全数据集，数据大的情况下，
    #     # 为了提高训练速度，用随机抽取的n张图片来训练，效果与全数据集相近
    #     # https://www.zhihu.com/question/32673260
    #     batch_size = 64
    #
    #     # 总的训练次数
    #     train_step = 2000
    #
    #     # 开始训练
    #     for i in range(train_step):
    #         # 从数据集中获取 输入和标签(也就是答案)
    #         x, label = self.data.train.next_batch(batch_size)
    #         # 每次计算train，更新整个网络
    #         # loss只是为了看到损失的大小，方便打印
    #         _, loss = self.sess.run([self.net.train, self.net.loss],
    #                                 feed_dict={self.net.x: x, self.net.label: label})
    #
    #         # 打印 loss，训练过程中将会看到，loss有变小的趋势
    #         # 代表随着训练的进行，网络识别图像的能力提高
    #         # 但是由于网络规模较小，后期没有明显下降，而是有明显波动
    #         if (i + 1) % 10 == 0:
    #             print('第%5d步，当前loss：%.2f' % (i + 1, loss))

    # v2版本
    def train(self):
        batch_size = 64
        train_step = 20000
        # 记录训练次数, 初始化为0
        step = 0

        # 每隔1000步保存模型
        save_interval = 1000

        # tf.train.Saver是用来保存训练结果的。
        # max_to_keep 用来设置最多保存多少个模型，默认是5
        # 如果保存的模型超过这个值，最旧的模型将被删除
        saver = tf.train.Saver(max_to_keep=5)

        # merge所有的summar node
        merged_summary_op = tf.summary.merge_all()
        # 可视化存储目录为当前文件夹下的log
        merged_writer = tf.summary.FileWriter("./log", self.sess.graph)

        ckpt = tf.train.get_checkpoint_state(CKPT_DIR)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(self.sess, ckpt.model_checkpoint_path)
            # 读取网络中的global_step的值，即当前已经训练的次数
            step = self.sess.run(self.net.global_step)
            print('Continue from')
            print('        -> Minibatch update : ', step)

        while step < train_step:
            x, label = self.data.train.next_batch(batch_size)
            _, loss, merged_summary = self.sess.run([self.net.train, self.net.loss, merged_summary_op],
                                    feed_dict={self.net.x: x, self.net.label: label})
            step = self.sess.run(self.net.global_step)

            if step % 100 == 0:
                # print('第%5d步，当前loss：%.2f' % (step, loss))
                merged_writer.add_summary(merged_summary, step)

            # 模型保存在ckpt文件夹下
            # 模型文件名最后会增加global_step的值，比如1000的模型文件名为 model-1000
            if step % save_interval == 0:
                saver.save(self.sess, CKPT_DIR + '/model', global_step=step)
                print('%s/model-%d saved' % (CKPT_DIR, step))

    def calculate_accuracy(self):
        test_x = self.data.test.images
        test_label = self.data.test.labels
        # 注意：与训练不同的是，并没有计算 self.net.train
        # 只计算了accuracy这个张量，所以不会更新网络
        # 最终准确率约为0.91
        accuracy = self.sess.run(self.net.accuracy,
                                 feed_dict={self.net.x: test_x, self.net.label: test_label})
        print("准确率: %.2f，共测试了%d张图片 " % (accuracy, len(test_label)))


if __name__ == "__main__":
    app = Train()
    app.train()
    app.calculate_accuracy()

# 运行后，会打印出如下结果
# 第   10步，当前loss：120.93
# 第   20步，当前loss：90.38
# 第   30步，当前loss：80.88
# 第   40步，当前loss：71.23
# 第   50步，当前loss：66.07
# 第   60步，当前loss：55.83
# 第   70步，当前loss：47.27
# 第   80步，当前loss：45.42
# 第   90步，当前loss：37.14
#     ...
# 第 2000步，当前loss：21.75
# 准确率: 0.91，共测试了10000张图片
