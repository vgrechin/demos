# -*- coding: utf-8 -*-

"""
Общие функции и утилиты

Created on 26 May 2015 by Slava Grechin
"""

from math import pi     #Число пи беспредельной точности

class Common:
    """
    Класс, содержащий общие функции и утилиты
    """
    @staticmethod
    def circumference(radius):
        """
        Метод вычисления длины окружности

        Attributes:
            :radius (qreal): Радиус окружности

        Returns:
            :qreal: Длина окружности данного радиуса
        """
        return 2 * pi * radius

    @staticmethod
    def circle_area(radius):
        """
        Метод вычисления площади круга

        Attributes:
            :radius (qreal): Радиус окружности

        Returns:
            :qreal: Площадь круга данного радиуса
        """
        return pi * radius * radius
