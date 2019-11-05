from PyQt5 import QtWidgets
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtCore import Qt, QPointF


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
        self.selectPen = QPen(Qt.red, 3)

    def drawPoint(self, point):
        """Add point to scene"""
        p = point.getPointItem()
        p.setPen(self.pen)
        self.addItem(p)

    def drawLine(self, line):
        """Add line to scene"""

        line = line.getLineItem()
        line.setPen(self.pen)
        self.addItem(line)

    def selectItem(self, x, y):
        item = self.items(QPointF(x, y))[0]
        item.setPen(self.selectPen)

        return item

    def unselectItem(self, item):
        item.setPen(self.pen)

    def deleteItem(self, item):
        self.removeItem(item)
