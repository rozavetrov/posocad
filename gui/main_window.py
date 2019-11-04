from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QToolBar, QToolButton, QLabel, QStatusBar
from PyQt5.QtGui import QIcon
from gui.scene import GraphicsView


class SuperCadUi(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Super Cad")
        self.setFixedSize(640, 480)

        # Create and set menu
        self.menu = self._createMenu()

        # Create and set tool bar
        self.activeInstrument = None
        self._createToolBar()

        # Create and set view
        self.centralWidget = GraphicsView()
        self.setCentralWidget(self.centralWidget)

        # Create and set status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

        return menu

    def _createToolBar(self):
        tools = QToolBar("Instruments")
        tools.setMinimumWidth(50)

        # Dict of Instruments
        self.instruments = {}

        # Creating instruments
        # Point
        point = QToolButton()
        point.str = "Point"
        point.setIcon(QIcon("./gui/icons/buttons/toolbar/point.svg"))
        # Line
        line = QToolButton()
        line.str = "Line"
        line.setIcon(QIcon("./gui/icons/buttons/toolbar/line.svg"))

        # Create instrument label
        self.instrumentLabel = QLabel()

        # Adding to tools bar
        tools.addWidget(point)
        tools.addWidget(line)
        tools.addWidget(self.instrumentLabel)

        # Adding instruments to dict
        self.instruments.update({
            "point": point,
            "line": line,
        })

        # Adding toolbar to main window
        self.addToolBar(Qt.LeftToolBarArea, tools)

        # Set active instrument
        self.setInstrument(self.instruments["point"])

    def setInstrument(self, instrument):
        self.activeInstrument = instrument
        self.instrumentLabel.setText(instrument.str)
