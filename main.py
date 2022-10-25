import sys

from PyQt5 import QtWidgets
import qdarktheme

from widgets.ConfigurationPage import ConfigurationElement

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox_main = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox_main)

        vbox_main.addWidget(ConfigurationElement("Power Continuity", "csv_template/power_continuity_template.csv"))
        vbox_main.addWidget(ConfigurationElement("Positive Circuit Continuity", "csv_template/positive_circuit_continuity_template.csv"))
        

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    App.setStyleSheet(qdarktheme.load_stylesheet("light"))
    window = MainWindow()
    window.show()
    window.setMaximumSize(window.size())
    sys.exit(App.exec())