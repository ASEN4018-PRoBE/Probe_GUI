import sys, json

from PyQt5 import QtWidgets
import qdarktheme

from widgets.ConfigurationPage import ConfigurationPage

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        with open("test_template/test_template.json","r") as f: self.test_template = json.loads(f.read())

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox_main = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox_main)

        vbox_main.addWidget(ConfigurationPage(self.test_template))
        

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    App.setStyleSheet(qdarktheme.load_stylesheet("light"))
    window = MainWindow()
    window.resize(780,500)
    window.show()
    sys.exit(App.exec())