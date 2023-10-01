import matplotlib.pyplot as plt
import numpy as np


def draw(intervals: list[float], holdings_time: list[float]):
    print('intervals: ', intervals)
    print('holding_time: ', holdings_time)
    # суммируем все значения из первого списка
    x_sum = sum(intervals)

    # создаем список координат x и y для построения графика
    x_coords = []
    y_coords = []
    for i in range(len(holdings_time)):
        if i == 0:
            x_coord = 0
            y_coord = 0
        else:
            x_coord = sum(intervals[:i - 1])
            y_coord = intervals[i - 1]
        x_coords.append(x_coord + holdings_time[i])
        y_coords.append(y_coord)

    # задаем параметры для столбцов
    width = 0.5
    bottom = 0

    # строим гистограмму
    plt.bar(x_coords, y_coords, width=width, bottom=bottom)

    # устанавливаем максимальную высоту гистограммы
    plt.ylim((0, max(intervals)))
    plt.minorticks_on()
    plt.xlim((0, x_sum))
    plt.grid(which='major')
    plt.grid(which='minor', linestyle=':')

    # Отображение графика
    plt.show()
