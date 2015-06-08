# -*- coding: utf-8 -*-

"""
Централизованния точка входа
для управление бизнес-логикой приложения

Created on 26 May 2015 by Slava Grechin
"""
from PyQt4 import QtCore    #Базовые компоненты
from common import *        #Общие утилиты
from maindialog import *    #Главное окно приложение
from circlescene import *   #Графическое изображение


class Controller(QtCore.QObject):
    """
    Класс управления бизнес-логикой приложения
    """
    def __init__(self, view):
        """
        Конструктор первоначальной настройки приложения

        Attributes:
            :view (MainDialog): Главное окно приложения
        """
        #Вызов онструктора базового класса QObject
        super(Controller, self).__init__()
        #: Ссылка на объект главного окна
        self.view = view
        #Установка заголовока главного окна
        self.view.setWindowTitle("Circumference calculator")
        #Инициализация графической сцены главного окна
        #объект сцены получает родителем главное окно
        #время его жизни теперь определяется таковым у главного окна
        self.view.setScene(scene = CircleScene(parent = self.view))
        #Обработка событий в PyQt базируется на механизме
        #слотов и сигналов. Когда главное окно сигнализурует о
        #готовности данных для вычислений испускается сигнал
        #calculated
        #Здесь этот сигнал соединяется с методом класса Controller
        #Метод calculate назыется слотом и предназначен для обработки
        #данных
        self.view.signal.calculated.connect(self.calculate)

    def calculate(self, radius):
        """
        Слот обновления радиуса и длины окружности

        Attributes:
            :radius (qreal): Радиус длины окружности
        """
        #Вызов метода обновления главного окна
        #circuit - длинна окружности
        #area - площадь окружности
        self.view.update(
              circuit = Common.circumference(radius)
            , area = Common.circle_area(radius))
