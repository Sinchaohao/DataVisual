# @Author:sch
# @Time:2022/07/18
# @File:rw_visual.py
# @software: PyCharm

import matplotlib.pyplot as plt

from random_walk import RandomWalk


# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolors='none', s=10)

    # 突出起点-终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    # 去坐标轴数值xticks,yticks
    plt.xticks([])
    plt.yticks([])
    # ax去四个边框
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # plt.axis('off') //相当于ax

    plt.show()

    keep_running = input("Make anthor walk? (y / n):")
    if keep_running == 'n':
        break