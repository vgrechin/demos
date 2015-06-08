# -*- coding: utf-8 -*-

"""
Главное окно приложения

Created on 26 May 2015 by Slava Grechin
"""

import sys                  #Системные функции
from PyQt4 import QtCore    #Базовые компоненты
from PyQt4 import QtGui     #Графические компоненты
from circlescene import *   #Графическая сцена
from ui_maindialog import * #Форма главного окна

class MainDialog(QtGui.QDialog):
    """
    Класс, обрабатывающий события главного окна
    """
    class Signal(QtCore.QObject):
        """
        Класс, содержащий сигналы главного окна
        """
        #: Сигнал для обработки введенных в окно данных
        #types - сигнатура сигнала
        #name - наименование сигнала
        calculated = QtCore.pyqtSignal('qreal', name = "calculated")

    def __init__(self):
        """
        Конструктор инициализации главного окна
        """
        super(MainDialog, self).__init__()
        #: Форма главного диалогового окна
        self.ui = Ui_MainDialog()
        #Инициализация формы главного окна
        self.ui.setupUi(self)
        #: Экземпляр хранилища сигналов главного окна
        self.signal = MainDialog.Signal()

        #Подключение сигнала 'pressed' кнопки 'Calculate
        #к слоту главного окна 'calculate'
        self.ui.pbutCalculate.pressed.connect(self.calculate)
        #Подключение сигнала 'pressed' кнопки 'Reset'
        #к слоту главного окна 'reset'
        self.ui.pbutReset.pressed.connect(self.reset)

    def setScene(self, scene):
        """
        Метод, инициализирующий графическую сцену на форме

        Attributes:
            :scene (CircleScene): Графическая сцена
        """
        self.ui.gviewCircle.setScene(scene)

    def calculate(self):
        """
        Слот, обрабатывающий нажатие кнопки 'Calculate'
        """
        #Получение значение радиуса с контрола формы
        radius = self.ui.dsboxRadius.value()
        #Получение значение диаметра с контрола формы
        diameter = self.ui.dsboxDiameter.value()
        #Радиус и диаметр не могут задаваться вместе
        if radius and diameter:
            #Окно сообщения, если заданы радиус и диаметр
            #Класс окна QMessageBox находится в модуле QtGui
            #Warning - тип окна сообщения
            #title - заголовок окна сообщения
            #text - содержание сообщения
            messageBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning
                , "Ambiguous dimension"
                , "You must enter either the radius or the diameter, not both")
            #Отображение модального диалога окна сообщения
            messageBox.exec_()
            #Очистка контролов формы
            self.reset()
        elif diameter:
            #Испускание сигнала 'calculated' с использованием диаметра
            self.signal.calculated.emit(diameter / 2)
        else:
            #Испускание сигнала 'calculated' с использованием радиуса
            self.signal.calculated.emit(radius)

    def reset(self):
        """
        Слот, обрабатывающий нажатие кнопки 'Reset'
        Очистка контролов формы
        """
        self.ui.dsboxRadius.setValue(0)
        self.ui.dsboxDiameter.setValue(0)
        self.ui.dsboxCircuit.setValue(0)
        self.ui.dsboxArea.setValue(0)

    def update(self, circuit, area):
        """
        Метод обновляющий значения длины и площади окружности
        Установка значение контролов формы
        """
        self.ui.dsboxCircuit.setValue(circuit)
        self.ui.dsboxArea.setValue(area)
