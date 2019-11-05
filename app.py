import sys

from PyQt5.QtWidgets import QApplication
from gui.main_window import SuperCadUi
from controllers.controller import CadController
from core.constraints import Constraints


def main():
    # Main app
    app = QApplication(sys.argv)

    # Show gui
    view = SuperCadUi()
    view.show()

    # Create model
    model = Constraints()

    # Create controller
    CadController(model, view)

    # Exec main event loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
