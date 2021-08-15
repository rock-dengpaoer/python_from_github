# 绘制散点图并设置其样式
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 使用颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# plt.scatter(x_values, y_values, s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 删除数据点的轮廓
# plt.scatter(x_values, y_values, edgecolors='none', s=40)

# 修改数据点的颜色
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# plt.scatter(x_values, y_values, c=(0, 0, 0.2), edgecolors='none', s=40)

plt.show()

# 自动保存图表
plt.savefig('squares_plot_scatter.png', bbox_inches='tight')
