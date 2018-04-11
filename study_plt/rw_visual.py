# encoding: utf-8
# 对随机散步类的调用，并且用plt可视化
import matplotlib.pyplot as plt
from study_plt.suijisanbu import RandomWalk
i = 0
while i < 3:

    rw = RandomWalk()
    point_num = list(range(rw.num_points))
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15, c=point_num, cmap=plt.cm.Blues, edgecolor='none')
    # plt.plot(rw.x_values, rw.y_values, linewidth=5)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.figure(figsize=(50, 20))
    plt.show()
    i += 1


