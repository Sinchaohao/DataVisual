# @Author:sch
# @Time:2022/07/18
# @File:scatter_squares.py
# @software: PyCharm
# description: 使用使 scatter() 绘制散点图并设置其样式

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [ x**2 for x in x_values]

plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=10)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])
plt.show()