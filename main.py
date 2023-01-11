import sys, json, qdarktheme
from PyQt6 import QtWidgets, QtCore

import global_vars
from widgets.NavigationPane import NavigationPane
from widgets.ConfigurationPage import ConfigurationPage
from widgets.TestResultsPage import TestResultsPage
from widgets.DetailedPlotsPage import DetailedPlotsPage
from widgets.StatusBar import StatusBar
from widgets.setup_gui import setup_gui
from interfaces.Tester import Tester

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ProBE")
        self.theme = global_vars.theme
        self.color_base = qdarktheme.load_palette(self.theme).base().color()
        self.color_light = qdarktheme.load_palette(self.theme).light().color()
        self.setStyleSheet(qdarktheme.load_stylesheet(self.theme))
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.config_filename = "test_template/test_template.json"
        self.setup_config(self.config_filename)

        # self.tester = Tester(self.test_config,self.test_results_page)

    def keyPressEvent(self, event) -> None:
        if event.key()==QtCore.Qt.Key.Key_Escape:
            quit()

    def setup_config(self, config_filename):
        with open(config_filename,"r") as f:
            self.test_config = json.loads(f.read())
        self.navigation_pane = NavigationPane(self.color_light)
        self.configuration_page = ConfigurationPage(self.test_config)
        self.test_results_page = TestResultsPage(self.test_config)
        self.detailed_plots_page = DetailedPlotsPage(self.test_config)
        self.status_bar = StatusBar()
        setup_gui(self)
    
    def load_config(self):
        path = "test_template/"
        config_filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open Configuration File", path, "JSON Files (*.json)")[0]
        if config_filename:
            self.config_filename = config_filename
            self.setup_config(self.config_filename)

    def save_as_config(self):
        path = "test_template/"
        save_filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save Configuration File", path+"/test_template.json", "JSON Files (*.json)")[0]
        if save_filename:
            with open(save_filename,"w") as f:
                f.write(json.dumps(self.test_config,indent=4))

    def save_config(self):
        save_filename = "test_template/test_template.json"
        with open(save_filename,"w") as f:
            f.write(json.dumps(self.test_config,indent=4))


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(1000,700)
    window.show()
    sys.exit(App.exec())