from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow
from core.gObjects import Point, Line, Parallelism


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

        # List of selected items
        self.selectedItems = set()

        # Current object
        self.curObjects = []

    def _connectSignals(self):
        """Connect signals and slots."""
        # Choosing current instrument
        for instrument in self._view.instruments.values():
            instrument.clicked.connect(lambda _: self._chooseInstrument())

        # Choosing active constraints
        for constraint in self._view.constraints.values():
            constraint.clicked.connect(lambda _: self._chooseConstraint())

        # Paint object
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
        constraint = self._view.activeConstraint.str
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
        point = Point(x, y)
        self.scene.drawPoint(point)

        return point

    def _drawLine(self, event, p1):
        x = event.scenePos().x()
        y = event.scenePos().y()

        p2 = self._drawPoint(x, y)

        p3 = Point(x + 10, y + 20)
        p4 = Point(x + 35, y + 40)

        line = Line(p1, p2)
        line2 = Line(p3, p4)
        self.scene.drawLine(line)
        self.scene.drawLine(line2)
        self.scene.mousePressEvent = lambda event: self._paintObject(event)

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

    def _deleteItems(self, event):
        if event.key() == Qt.Key_Backspace:
            for item in self.selectedItems:
                self._view.centralWidget.scene.deleteItem(item)
            self.selectedItems.clear()
