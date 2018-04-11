# encoding: utf-8
# 了解了一下plot绘制折线图和scatter绘制散点图的基本用法
import matplotlib.pyplot as plt
import matplotlib
'''
squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=2)
plt.title("hello")
plt.xlabel("value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis="both", labelsize=14)
plt.show()
'''
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.title("ninini", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of value", fontsize=14)
# plt.scatter(x_values, y_values, edgecolors='none', s=100)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=100)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.show()
