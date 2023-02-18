import os, json, qdarktheme, numpy
from PyQt6 import QtWidgets, QtCore

import global_vars
from widgets.NavigationPane import NavigationPane
from widgets.ConfigurationPage import ConfigurationPage
from widgets.TestResultsPage import TestResultsPage
from widgets.DetailedPlotsPage import DetailedPlotsPage
from widgets.HelpAboutPage import HelpAboutPage
from widgets.StatusBar import StatusBar
from interfaces.TestController import TestController

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

    def keyPressEvent(self, event) -> None:
        if event.key()==QtCore.Qt.Key.Key_Escape or event.key()==QtCore.Qt.Key.Key_Q: quit()

    def setup_config(self, config_filename):
        with open(config_filename,"r") as f:
            self.test_config = json.loads(f.read())
        self.navigation_pane = NavigationPane(self.color_light)
        self.configuration_page = ConfigurationPage(self.test_config)
        self.test_results_page = TestResultsPage(self.test_config)
        self.detailed_plots_page = DetailedPlotsPage(self.test_config)
        self.help_about_page = HelpAboutPage()
        self.status_bar = StatusBar()
        self.test_controller = TestController(self.test_config,self)
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

    def export_csv(self):
        if not self.test_controller.test_complete:
            global_vars.pop_information("Test not complete! Export when all tests are complete.")
            return
        save_dir = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select csv Save Directory"))
        if save_dir is None: return
        print(save_dir)
        dict_csv_str = self.test_controller.test_storage.to_csv()
        for test_function in global_vars.test_functions:
            os.mkdir("battery_test_csv_results")
            with open(save_dir+"/battery_test_csv_results/"+test_function+".csv","w") as f:
                f.write(dict_csv_str[test_function])

def setup_gui(self:MainWindow):
    if self.central_widget.layout():
        # reparent the current layout of central_widget's layout
        QtWidgets.QWidget().setLayout(self.central_widget.layout())
    hbox_main = QtWidgets.QHBoxLayout()
    self.central_widget.setLayout(hbox_main)

    self.stacked_layout = QtWidgets.QStackedLayout()
    
    self.navigation_pane.recolor(0,self.color_base,self.color_light)
    hbox_main.addWidget(self.navigation_pane)
    def btn_configuration_clicked(event):
        self.stacked_layout.setCurrentIndex(0)
        self.navigation_pane.recolor(0, self.color_base, self.color_light)
    def btn_test_results_clicked(event):
        self.stacked_layout.setCurrentIndex(1)
        self.navigation_pane.recolor(1, self.color_base, self.color_light)
    def btn_detailed_plots_clicked(event):
        self.stacked_layout.setCurrentIndex(2)
        self.navigation_pane.recolor(2, self.color_base, self.color_light)
    def btn_help_about_clicked(event):
        self.stacked_layout.setCurrentIndex(3)
        self.navigation_pane.recolor(3, self.color_base, self.color_light)
    self.navigation_pane.btn_configuration.mousePressEvent = btn_configuration_clicked
    self.navigation_pane.btn_test_results.mousePressEvent = btn_test_results_clicked
    self.navigation_pane.btn_detailed_plots.mousePressEvent = btn_detailed_plots_clicked
    self.navigation_pane.btn_help_about.mousePressEvent = btn_help_about_clicked
    self.navigation_pane.btn_start.clicked.connect(self.test_controller.start)
    self.navigation_pane.btn_stop.clicked.connect(self.test_controller.stop)

    vertical_line = QtWidgets.QFrame()
    vertical_line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
    vertical_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
    hbox_main.addWidget(vertical_line)
    
    self.configuration_page.btn_load.clicked.connect(self.load_config)
    self.configuration_page.btn_save_as.clicked.connect(self.save_as_config)
    self.configuration_page.btn_save.clicked.connect(self.save_config)

    self.test_results_page.btn_export.clicked.connect(self.export_csv)
    self.detailed_plots_page.btn_export.clicked.connect(self.export_csv)

    self.stacked_layout.addWidget(self.configuration_page)
    self.stacked_layout.addWidget(self.test_results_page)
    self.stacked_layout.addWidget(self.detailed_plots_page)
    self.stacked_layout.addWidget(self.help_about_page)

    hbox_main.addLayout(self.stacked_layout)

    self.setStatusBar(self.status_bar)

    # templates for presentation
    self.status_bar.set_message(False,"n/a","n/a","n/a")
    self.status_bar.progress_bar.setValue(0)
    x = numpy.linspace(0,2*numpy.pi)
    y = numpy.sin(x)
    self.detailed_plots_page.plot(x,y)