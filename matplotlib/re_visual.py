# 绘制随机漫步图
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例,并将其包含的点都绘制出来
while True:
    # rw = RandomWalk()

    # 增加一下点数
    rw = RandomWalk(5000)

    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure( figsize=(10, 6))

    point_numbers = list(range(rw.num_points))

    # 给点上色
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴

    # 图片看不到，坐标轴并未隐藏
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    # 修改的第一种方法
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    # 修改的第二种方法, 将隐藏坐标轴放在上色前面
    # a = plt.axes()
    # a.xaxis.set_visible(False)
    # a.yaxis.set_visible(False)
    # 原理分析：get_xaxis()里边的注释是不建议使用这个函数的，应该是一个bug，
    # 换成建议格式之后还是不行，应该在一开始就要把坐标轴隐藏掉

    plt.show()
    keep_running = input("continue?(y/n)")
    if keep_running == 'n':
        break
    elif keep_running == 'y':
        continue
    else:
        print("sorry, please try again")
        keep_running = input("continue?(y/n)")
