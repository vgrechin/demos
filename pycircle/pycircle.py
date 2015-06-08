#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Запускаемый файл для демонстратора PyQt

Created on 25 May 2015 by Slava Grechin
"""

import sys                  #Системные функции
from PyQt4 import QtCore    #Базовые компоненты
from PyQt4 import QtGui     #Компоненты графического интерфейса
from maindialog import *    #Модуль главного окна калькулятора
from controller import *    #Контроллер приложения

def main():
    """
    Главная функция приложения,
    запускает калькулятор длинны и площади окружности
    """

    # Каждое приложение должно создать объект класса QApplication
    # Класс QApplication находится в модуле QtGui
    # sys.argv - список аргументов командной строки
    app = QtGui.QApplication(sys.argv)

    #MainDialog - базовый класс для всех объектов интерфейса
    #объект view не имеет родителя, и поэтому становится главным окном
    view = MainDialog()

    #Contoller - класс бизнес-логики приложения
    #объект doc получает MainDialog для соединения слотов с сигналами
    doc = Controller(view)

    view.show()             #Отобразить главный диалог на экране

    sys.exit(app.exec_())   #Запуск основного цикла приложения

if __name__ == '__main__':  #Выполняется запуск модуля, как программы
    main()                  #Вызов главной функции приложения
