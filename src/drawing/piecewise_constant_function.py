import math

import matplotlib.pyplot as plt
import numpy as np


def draw(intervals: list[float], holdings_time: list[float]):
    # суммируем все значения из первого списка
    x_sum = sum(intervals) + holdings_time[-1]

    # создаем список координат x и y для построения графика
    x_coords = []
    y_coords = []
    for i in range(len(holdings_time)):
        if i == 0:
            x_coord = sum(intervals[:i])  # откладываем i-ое значение из первого списка
            y_coord = 0
        else:
            x_coord = 0
            y_coord = intervals[i - 1]  # создаем список длины i-го элемента из второго списка
        x_coords.append(x_coord + holdings_time[i])
        y_coords.append(y_coord)

    # строим график
    plt.hist(x_coords, bins=np.arange(0, x_sum, x_sum / len(holdings_time)), align='left')
    plt.xlabel('Отчёт времени')
    plt.ylabel('Номер элемента')
    plt.show()
