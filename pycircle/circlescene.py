# -*- coding: utf-8 -*-

"""
Графическая сцена главного окна

Created on 26 May 2015 by Slava Grechin
"""

from PyQt4 import QtCore    #Базовые компоненты
from PyQt4 import QtGui     #Графические компоненты

class CircleScene(QtGui.QGraphicsScene):
    """
    Класс, размещающий графические объекты на сцене
    """
    default_arrow    = 6                  #: Размерность стрелки
    default_radius   = 100                #: Размерность радиуса
    default_diameter = 2 * default_radius #: Размерность диаметра

    def __init__(self
            , parent    = None
            , arrow     = default_arrow
            , radius    = default_radius
            , diameter  = default_diameter):
        """
        Конструктор графической сцены главного окна

        Attributes:
            :parent (QObject):  Родительский объект сцены
            :arrow (int):       Размер стрелки на сцене
            :radius (int):      Размер изображения радиуса
            :diameter (int):    Размер изображения диаметра
        """
        super(CircleScene, self).__init__(parent)

        #: Изображение круга на сцене
        self.circle = self.addEllipse(0, 0, diameter, diameter)

        #: Изображение горизонтальной линии радиуса на сцене
        self.radius = self.addLine(radius, radius, diameter, radius)
        polygonLeft = QtGui.QPolygonF(
            [ QtCore.QPointF(radius, radius)
            , QtCore.QPointF(radius + arrow, radius + arrow / 2)
            , QtCore.QPointF(radius + arrow, radius - arrow / 2)])
        #: Изображение левой стрелки линии радиуса
        self.leftArrow = self.addPolygon(
              polygonLeft
            , QtGui.QPen()
            , QtGui.QBrush(QtCore.Qt.black))

        polygonRight = QtGui.QPolygonF(
            [ QtCore.QPointF(diameter, radius)
            , QtCore.QPointF(diameter - arrow, radius + arrow / 2)
            , QtCore.QPointF(diameter - arrow, radius - arrow / 2)])
        #: Изображение правой стрелки линии радиуса
        self.rightArrow = self.addPolygon(
              polygonRight
            , QtGui.QPen()
            , QtGui.QBrush(QtCore.Qt.black))

        #: Изображение вертикальной линии диаметра на сцене
        self.diameter = self.addLine(radius, 0, radius, diameter)
        polygonTop = QtGui.QPolygonF(
            [ QtCore.QPointF(radius, 0)
            , QtCore.QPointF(radius + arrow / 2, arrow)
            , QtCore.QPointF(radius - arrow / 2, arrow)])
        #: Изображение верхней стрелки линии диаметра
        self.topArrow = self.addPolygon(
              polygonTop
            , QtGui.QPen()
            , QtGui.QBrush(QtCore.Qt.black))

        polygonBottom = QtGui.QPolygonF(
            [ QtCore.QPointF(radius, diameter)
            , QtCore.QPointF(radius + arrow / 2, diameter - arrow)
            , QtCore.QPointF(radius - arrow / 2, diameter - arrow)])
        #: Изображение нижней стрелки линии диаметра
        self.bottomArrow = self.addPolygon(
              polygonBottom
            , QtGui.QPen()
            , QtGui.QBrush(QtCore.Qt.black))

        #: Текстовая метка линии радиуса
        self.radiusLabel = self.addText("Radius")
        #: Текстовая метка линии диаметра
        self.diameterLabel = self.addText("Diameter")
        #Размещение метки радиуса на сцене
        self.radiusLabel.setPos(
              radius + self.radiusLabel.boundingRect().width() / 2
            , radius)
        #Размещение метки диаметра на сцене
        self.diameterLabel.setPos(
              radius - self.diameterLabel.boundingRect().height()
            , radius + self.diameterLabel.boundingRect().width() / 2)
        #Поворот метки диаметра
        self.diameterLabel.rotate(270)

