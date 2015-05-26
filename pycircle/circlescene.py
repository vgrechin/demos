from PyQt4 import QtCore, QtGui

class CircleScene(QtGui.QGraphicsScene):
    default_arrow       = 6
    default_radius      = 100
    default_diameter    = 2 * default_radius

    def __init__(self
            , parent    = None
            , arrow     = default_arrow
            , radius    = default_radius
            , diameter  = default_diameter):
        super(CircleScene, self).__init__(parent)

        self.circle = self.addEllipse(0, 0, diameter, diameter)

        self.radius = self.addLine(radius, radius, diameter, radius)
        polygonLeft = QtGui.QPolygonF(
            [ QtCore.QPointF(radius, radius)
            , QtCore.QPointF(radius + arrow, radius + arrow / 2)
            , QtCore.QPointF(radius + arrow, radius - arrow / 2)])
        self.leftArrow = self.addPolygon(
              polygonLeft
            , QtGui.QPen()
            , QtGui.QBrush(QtCore.Qt.black))

        polygonRight = QtGui.QPolygonF(
            [ QtCore.QPointF(diameter, radius)
            , QtCore.QPointF(diameter - arrow, radius + arrow / 2)
            , QtCore.QPointF(diameter - arrow, radius - arrow / 2)])
        self.rightArrow = self.addPolygon(
              polygonRight
            , QtGui.QPen()
            , QtGui.QBrush(QtCore.Qt.black))

        self.diameter = self.addLine(radius, 0, radius, diameter)
        polygonTop = QtGui.QPolygonF(
            [ QtCore.QPointF(radius, 0)
            , QtCore.QPointF(radius + arrow / 2, arrow)
            , QtCore.QPointF(radius - arrow / 2, arrow)])
        self.topArrow = self.addPolygon(
              polygonTop
            , QtGui.QPen()
            , QtGui.QBrush(QtCore.Qt.black))

        polygonBottom = QtGui.QPolygonF(
            [ QtCore.QPointF(radius, diameter)
            , QtCore.QPointF(radius + arrow / 2, diameter - arrow)
            , QtCore.QPointF(radius - arrow / 2, diameter - arrow)])
        self.bottomArrow = self.addPolygon(
              polygonBottom
            , QtGui.QPen()
            , QtGui.QBrush(QtCore.Qt.black))

        self.radiusLabel = self.addText("Radius")
        self.diameterLabel = self.addText("Diameter")
        self.radiusLabel.setPos(
              radius + self.radiusLabel.boundingRect().width() / 2
            , radius)
        self.diameterLabel.setPos(
              radius - self.diameterLabel.boundingRect().height()
            , radius + self.diameterLabel.boundingRect().width() / 2)
        self.diameterLabel.rotate(270)

