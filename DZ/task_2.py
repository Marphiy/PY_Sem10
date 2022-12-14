"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""

import os
from non_neg_is_dig import NonNegativeIsDigit as nnid


def clear_screen():
    os.system('cls' if os == 'nt' else 'clear')


class Road:
    __weight = 25
    r_length = nnid()
    r_width = nnid()

    def __init__(self, r_length, r_width, r_thickness=0.05):
        self.r_length = r_length
        self.r_width = r_width
        self.r_thickness = 0.05

    def get_total_weight(self):
        print(f'Суммарная масса дорожного полотна составит '
              f'{self.r_length * self.r_width * self.__weight * self.r_thickness}кг.')



# clear_screen()
# r = Road(-8, 4)
r = Road('jhgj', 4)
# r = Road(17, 4)
r.get_total_weight()
