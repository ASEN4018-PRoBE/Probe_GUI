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
        
        self.configuration_page = ConfigurationPage(self.test_template)
        self.configuration_page.btn_load.clicked.connect(self.load_config)
        self.configuration_page.btn_save.clicked.connect(self.save_config)
        vbox_main.addWidget(self.configuration_page)
    
    def load_config(self): # TODO
        print("loading config")

    def save_config(self): # TODO
        print("saving config")



if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    App.setStyleSheet(qdarktheme.load_stylesheet("dark"))
    window = MainWindow()
    window.resize(780,500)
    window.show()
    sys.exit(App.exec())