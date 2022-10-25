import sys, json

from PyQt5 import QtWidgets
import qdarktheme

from widgets.ConfigurationPage import ConfigurationElement

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        with open("test_template/test_template.json","r") as f: self.test_template = json.loads(f.read())

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox_main = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox_main)

        vbox_main.addWidget(ConfigurationElement("Power Continuity", self.test_template["power_continuity"]))
        vbox_main.addWidget(ConfigurationElement("Positive Circuit Continuity", self.test_template["positive_circuit_continuity"]))
        

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    App.setStyleSheet(qdarktheme.load_stylesheet())
    window = MainWindow()
    window.show()
    sys.exit(App.exec())