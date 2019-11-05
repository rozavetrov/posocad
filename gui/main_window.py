from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QToolBar, QToolButton, QLabel, QStatusBar, QWidget
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
        self.activeConstraint = None
        self._createToolBar()

        # Create and set view
        self.centralWidget = GraphicsView()
        self.setCentralWidget(self.centralWidget)

        # Create and set status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")

    def _createMenu(self):
        """Menu"""
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

        return menu

    def _createToolBar(self):
        """Tool Bar"""
        tools = QToolBar("Instruments")
        tools.setMinimumWidth(125)

        # Dict of Instruments
        self.instruments = {}
        # Dict of Constraints
        self.constraints = {}

        # Creating instruments
        # Point
        point = QToolButton()
        point.str = "Point"
        point.setIcon(QIcon("./gui/icons/buttons/toolbar/point.svg"))
        # Line
        line = QToolButton()
        line.str = "Line"
        line.setIcon(QIcon("./gui/icons/buttons/toolbar/line.svg"))
        # Select
        select = QToolButton()
        select.str = "Select"
        select.setIcon(QIcon("./gui/icons/buttons/toolbar/select.svg"))

        # Creating constrains instruments
        # Parallelism
        parallelism = QToolButton()
        parallelism.str = "Parallelism"
        parallelism.setIcon(QIcon("./gui/icons/buttons/toolbar/parallelism.svg"))
        # Perpendicularity
        perpendicularity = QToolButton()
        perpendicularity.str = "Perpendicularity"
        perpendicularity.setIcon(QIcon("./gui/icons/buttons/toolbar/perpendicularity.svg"))

        # Create instrument label
        self.instrumentLabel = QLabel()
        # Create constraint label
        self.constraintLabel = QLabel()

        # Spacer widget
        spacer = QWidget()
        spacer.setFixedHeight(50)

        # Adding to tools bar
        # Instruments
        tools.addWidget(QLabel("Instruments"))
        tools.addWidget(point)
        tools.addWidget(line)
        tools.addWidget(select)
        tools.addWidget(self.instrumentLabel)

        tools.addWidget(spacer)

        # Constraints
        tools.addWidget(QLabel("Constraints"))
        tools.addWidget(parallelism)
        tools.addWidget(perpendicularity)
        tools.addWidget(self.constraintLabel)

        # Adding instruments to dict
        self.instruments.update({
            "point": point,
            "line": line,
            "select": select
        })
        # Adding constraints to dict
        self.constraints.update({
            "parallelism": parallelism,
            "perpendicularity": perpendicularity
        })

        # Adding toolbar to main window
        self.addToolBar(Qt.LeftToolBarArea, tools)

        # Set active instrument
        self.setInstrument(self.instruments["point"])

    def setInstrument(self, instrument):
        """Set active instrument"""
        self.activeInstrument = instrument
        self.instrumentLabel.setText(instrument.str)

    def setConstraint(self, constraint):
        """Set active constraint"""
        self.activeConstraint = constraint
        self.constraintLabel.setText(constraint.str)
