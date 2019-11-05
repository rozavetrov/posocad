from PyQt5.QtCore import QPointF, QRectF, QLineF
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsLineItem


class MyPoint(QPointF):
    def __init__(self, x, y):
        QPointF.__init__(self, x, y)

    def getPointItem(self):
        return QGraphicsEllipseItem(QRectF(self.x() - 3, self.y() - 3, 6, 6))

    def __str__(self):
        return f"({self.x()}, {self.y()})"


class MyLine(QLineF):
    def __init__(self, point1=None, point2=None):
        self.mypoint1 = point1
        self.mypoint2 = point2
        QLineF.__init__(self, point1, point2)

    def getLineItem(self):
        return QGraphicsLineItem(self.mypoint1.x(), self.mypoint1.y(), self.mypoint2.x(), self.mypoint2.y())

    def __str__(self):
        return f"p1={self.mypoint1} p2={self.mypoint2}"
