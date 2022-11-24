import sys, json

from PyQt5 import QtWidgets
import qdarktheme

from widgets.NavigationPane import NavigationPane
from widgets.ConfigurationPage import ConfigurationPage
from widgets.TestReultsPage import TestResultsPage
from widgets.DetailedPlotsPage import DetailedPlotsPage
from widgets.StatusBar import StatusBar
from widgets.setup_gui import setup_gui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ProBE")
        self.theme = "light"
        self.color_base = qdarktheme.load_palette(self.theme).base().color()
        self.color_light = qdarktheme.load_palette(self.theme).light().color()

        with open("test_template/test_template.json","r") as f: self.test_template = json.loads(f.read())
        
        self.navigation_pane = NavigationPane(self.color_light)
        self.configuration_page = ConfigurationPage(self.test_template)
        self.test_results_page = TestResultsPage(self.test_template)
        self.detailed_plots_page = DetailedPlotsPage(self.test_template)
        self.status_bar = StatusBar()
        setup_gui(self)
    
    def load_config(self): # TODO
        path = "test_template/"
        config_file = QtWidgets.QFileDialog.getOpenFileName(self, "Open Configuration File", path, "JSON Files (*.json)")[0]
        if config_file:
            pass

    def save_as_config(self): # TODO
        path = "test_template/"
        save_filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save Configuration File", path+"/test_template.json", "JSON Files (*.json)")[0]
        if save_filename:
            pass

    def save_config(self): # TODO
        pass


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(1200,800)
    window.show()
    sys.exit(App.exec())