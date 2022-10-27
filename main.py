import sys, json

from PyQt5 import QtWidgets
import qdarktheme

from widgets.ConfigurationPage import ConfigurationPage
from widgets.TestReultPage import TestResultPage

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
        #vbox_main.addWidget(self.configuration_page)

        self.test_result_page = TestResultPage(self.test_template)
        self.test_result_page.element_dict["Power Continuity"].append_test_result("Pin1","Pin2","10 V",False)
        self.test_result_page.element_dict["Positive Circuit Continuity"].append_test_result("Pin1","Pin2","0.5 Ohm",True)
        self.test_result_page.element_dict["Positive Circuit Continuity"].append_test_result("Pin1","Pin2","0.6 Ohm",True)
        self.test_result_page.element_dict["Positive Circuit Continuity"].append_test_result("Pin1","Pin2","1.1 Ohm",False)
        self.test_result_page.element_dict["Positive Circuit Continuity"].append_test_result("Pin1","Pin2","0.5 Ohm",True)
        vbox_main.addWidget(self.test_result_page)
    
    def load_config(self): # TODO
        path = "test_template/"
        config_file = QtWidgets.QFileDialog.getOpenFileName(self,"Open Configuration File",path,"JSON Files (*.json)")[0]
        if config_file:
            pass

    def save_config(self): # TODO
        path = "test_template/"
        save_filename = QtWidgets.QFileDialog.getSaveFileName(self,"Save Configuration File",path+"/test_template.json","JSON Files (*.json)")[0]
        if save_filename:
            pass


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    App.setStyleSheet(qdarktheme.load_stylesheet("light"))
    window = MainWindow()
    window.resize(780,600)
    window.show()
    sys.exit(App.exec())