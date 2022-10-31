import sys, json

from PyQt5 import QtWidgets
from PyQt5 import QtCore
import qdarktheme

from widgets.ConfigurationPage import ConfigurationPage
from widgets.TestReultPage import TestResultPage

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProBE GUI")
        with open("test_template/test_template.json","r") as f: self.test_template = json.loads(f.read())

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        hbox_main = QtWidgets.QHBoxLayout()
        central_widget.setLayout(hbox_main)

        self.stacked_layout = QtWidgets.QStackedLayout()
        
        self.configuration_page = ConfigurationPage(self.test_template)
        self.configuration_page.btn_load.clicked.connect(self.load_config)
        self.configuration_page.btn_save_as.clicked.connect(self.save_as_config)
        self.configuration_page.btn_save.clicked.connect(self.save_config)
        self.stacked_layout.addWidget(self.configuration_page)

        self.test_result_page = TestResultPage(self.test_template)
        self.test_result_page.element_dict["Power Continuity"].append_test_result("Pin1","Pin2","10 V",False)
        self.test_result_page.element_dict["Positive Circuit Continuity"].append_test_result("Pin1","Pin2","0.5 Ohm",True)
        self.test_result_page.element_dict["Positive Circuit Continuity"].append_test_result("Pin1","Pin2","0.6 Ohm",True)
        self.test_result_page.element_dict["Positive Circuit Continuity"].append_test_result("Pin1","Pin2","1.1 Ohm",False)
        self.test_result_page.element_dict["Positive Circuit Continuity"].append_test_result("Pin1","Pin2","0.5 Ohm",True)
        self.stacked_layout.addWidget(self.test_result_page)

        hbox_main.addLayout(self.stacked_layout)
    
    def load_config(self): # TODO
        path = "test_template/"
        config_file = QtWidgets.QFileDialog.getOpenFileName(self,"Open Configuration File",path,"JSON Files (*.json)")[0]
        if config_file:
            pass

    def save_as_config(self): # TODO
        path = "test_template/"
        save_filename = QtWidgets.QFileDialog.getSaveFileName(self,"Save Configuration File",path+"/test_template.json","JSON Files (*.json)")[0]
        if save_filename:
            pass

    def save_config(self): # TODO
        pass
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Space:
            page_index = self.stacked_layout.currentIndex()
            if page_index==self.stacked_layout.count()-1: page_index = 0
            else: page_index += 1
            self.stacked_layout.setCurrentIndex(page_index)
        event.accept()


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    App.setStyleSheet(qdarktheme.load_stylesheet("dark"))
    window = MainWindow()
    window.resize(780,600)
    window.show()
    sys.exit(App.exec())