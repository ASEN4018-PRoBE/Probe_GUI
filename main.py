import sys
from PyQt6 import QtWidgets

from widgets.MainWindow import MainWindow

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(1200,840)
    window.show()
    sys.exit(App.exec())