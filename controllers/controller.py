from PyQt5.QtCore import pyqtSlot, QRectF, QLineF
from PyQt5.QtWidgets import QMainWindow, QGraphicsEllipseItem


class CadController(QMainWindow):
    """Main controller class."""

    def __init__(self, model, view, parent=None):
        super().__init__(parent)
        # Controller initializer
        self._view = view
        self._calculator = model

        # Connect signals and slots
        self._connectSignals()

        # Drawing flag
        self.isDrawing = False

    def _connectSignals(self):
        """Connect signals and slots."""
        # Choosing current instrument
        self._view.instruments["point"].clicked.connect(lambda _: self._chooseInstrument())
        self._view.instruments["line"].clicked.connect(lambda _: self._chooseInstrument())

        # Paint object: point or line
        self._view.centralWidget.scene.mousePressEvent = lambda event: self._paintObject(event)

    @pyqtSlot()
    def _chooseInstrument(self):
        self._view.setInstrument(self._view.sender())

    def _paintObject(self, event):
        """Draw objects"""
        x = event.scenePos().x()
        y = event.scenePos().y()

        # Draw point
        self._view.centralWidget.scene.drawPoint(x, y)

        # Draw line
        if self._view.activeInstrument.str == "Line":
            if not self.isDrawing:
                self.point1 = (x, y)
                self.isDrawing = True
            else:
                self.point2 = (x, y)
                self._view.centralWidget.scene.drawLine(self.point1, self.point2)
                self.isDrawing = False
