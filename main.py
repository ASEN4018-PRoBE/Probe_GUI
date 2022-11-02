import sys, json

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import qdarktheme

from widgets.NavigationPane import NavigationPane
from widgets.ConfigurationPage import ConfigurationPage
from widgets.TestReultsPage import TestResultsPage
from widgets.DetailedPlotsPage import DetailedPlotsPage
from widgets.StatusBar import StatusBar

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProBE")
        with open("test_template/test_template.json","r") as f: self.test_template = json.loads(f.read())

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        hbox_main = QtWidgets.QHBoxLayout()
        central_widget.setLayout(hbox_main)

        self.stacked_layout = QtWidgets.QStackedLayout()
        
        self.navigation_pane = NavigationPane()
        hbox_main.addWidget(self.navigation_pane)
        self.navigation_pane.btn_configuration.mousePressEvent = self.btn_configuration_clicked
        self.navigation_pane.btn_test_results.mousePressEvent = self.btn_test_results_clicked
        self.navigation_pane.btn_detailed_plots.mousePressEvent = self.btn_detailed_plots_clicked

        vertical_line = QtWidgets.QFrame()
        vertical_line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        vertical_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        hbox_main.addWidget(vertical_line)
        
        self.configuration_page = ConfigurationPage(self.test_template)
        self.configuration_page.btn_load.clicked.connect(self.load_config)
        self.configuration_page.btn_save_as.clicked.connect(self.save_as_config)
        self.configuration_page.btn_save.clicked.connect(self.save_config)
        self.stacked_layout.addWidget(self.configuration_page)

        self.test_results_page = TestResultsPage(self.test_template)
        self.test_results_page.element_dict["Power Continuity"].append_test_result("Pin1","Pin2","10 V",False)
        self.test_results_page.element_dict["Power Continuity"].append_test_result("Pin1","Pin2","28 V",True)
        self.stacked_layout.addWidget(self.test_results_page)

        self.detailed_plots_page = DetailedPlotsPage(self.test_template)
        self.stacked_layout.addWidget(self.detailed_plots_page)

        hbox_main.addLayout(self.stacked_layout)

        self.status_bar = StatusBar()
        self.setStatusBar(self.status_bar)
    
    def btn_configuration_clicked(self, event):
        self.stacked_layout.setCurrentIndex(0)
    
    def btn_test_results_clicked(self, event):
        self.stacked_layout.setCurrentIndex(1)

    def btn_detailed_plots_clicked(self, event):
        self.stacked_layout.setCurrentIndex(2)
    
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


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    App.setStyleSheet(qdarktheme.load_stylesheet("dark"))
    window = MainWindow()
    window.resize(1000,700)
    window.show()
    sys.exit(App.exec())