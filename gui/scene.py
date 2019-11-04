from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtCore import Qt, QRectF, QLineF
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsLineItem


class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsView.__init__(self, parent=parent)
        # Creating scene
        self.scene = GraphicsScene(self)
        self.setScene(self.scene)
        # Creating pen


class GraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent=parent)
        # Set painting area
        self.setSceneRect(-100, -100, 200, 200)

        # Set painting instrument
        self.pen = QPen(Qt.black, 3)
        self.brush = QBrush(Qt.black)

    def drawPoint(self, x, y):
        """Creating point"""
        point = QGraphicsEllipseItem(QRectF(x - 3, y - 3, 6, 6))
        point.setPen(self.pen)
        self.addItem(point)

    def drawLine(self, point1, point2):
        line = QGraphicsLineItem(*point1, *point2)
        line.setPen(self.pen)
        self.addItem(line)
