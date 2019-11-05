from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow
from core.gObjects import MyPoint, MyLine


class CadController(QMainWindow):
    """Main controller class."""
    def __init__(self, model, view, parent=None):
        super().__init__(parent)
        # Controller initializer
        self._view = view
        self._calculator = model
        # Drawing scene
        self.scene = self._view.centralWidget.scene

        # Connect signals and slots
        self._connectSignals()

        # Drawing flag
        self.isDrawing = False

        # List of selected items
        self.selectedItems = set()

        # Current object
        self.curObjects = []

    def _connectSignals(self):
        """Connect signals and slots."""
        # Choosing current instrument
        self._view.instruments["point"].clicked.connect(lambda _: self._chooseInstrument())
        self._view.instruments["line"].clicked.connect(lambda _: self._chooseInstrument())
        self._view.instruments["select"].clicked.connect(lambda _: self._chooseInstrument())

        # Choosing active constraints
        self._view.constraints["parallelism"].clicked.connect(lambda _: self._chooseConstraint())
        self._view.constraints["perpendicularity"].clicked.connect(lambda _: self._chooseConstraint())

        # Paint object: point or line
        self._view.centralWidget.scene.mousePressEvent = lambda event: self._paintObject(event)

        # Delete selected items
        self._view.centralWidget.scene.keyPressEvent = lambda event: self._deleteItems(event)

    @pyqtSlot()
    def _chooseInstrument(self):
        self._view.setInstrument(self._view.sender())

    @pyqtSlot()
    def _chooseConstraint(self):
        self._view.setConstraint(self._view.sender())

    def _paintObject(self, event):
        """Draw objects"""
        # Active instrument
        instrument = self._view.activeInstrument.str
        # Mouse position
        x = event.scenePos().x()
        y = event.scenePos().y()

        # Draw point
        if instrument == "Point":
            self._drawPoint(x, y)

        # Draw line
        if instrument == "Line":
            p1 = self._drawPoint(x, y)
            self.scene.mousePressEvent = lambda event: self._drawLine(event, p1)

        # Select object
        if instrument == "Select":
            self._selectItem(x, y)

    def _drawPoint(self, x, y):
        point = MyPoint(x, y)
        self.scene.drawPoint(point)

        return point

    def _selectItem(self, x, y):
        try:
            item = self.scene.selectItem(x, y)
            if item not in self.selectedItems:
                self.selectedItems.add(item)
            else:
                self.scene.unselectItem(item)
                self.selectedItems.remove(item)
        except IndexError as e:
            pass

    def _drawLine(self, event, p1):
        x = event.scenePos().x()
        y = event.scenePos().y()

        p2 = self._drawPoint(x, y)
        line = MyLine(p1, p2)
        self.scene.drawLine(line)
        self.scene.mousePressEvent = lambda event: self._paintObject(event)

    def _deleteItems(self, event):
        if event.key() == Qt.Key_Backspace:
            for item in self.selectedItems:
                self._view.centralWidget.scene.deleteItem(item)
            self.selectedItems.clear()
