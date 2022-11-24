import qdarktheme

from PyQt5 import QtWidgets

def setup_gui(self):
    self.setStyleSheet(qdarktheme.load_stylesheet(self.theme))
    central_widget = QtWidgets.QWidget()
    self.setCentralWidget(central_widget)
    hbox_main = QtWidgets.QHBoxLayout()
    central_widget.setLayout(hbox_main)

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
    self.navigation_pane.btn_configuration.mousePressEvent = btn_configuration_clicked
    self.navigation_pane.btn_test_results.mousePressEvent = btn_test_results_clicked
    self.navigation_pane.btn_detailed_plots.mousePressEvent = btn_detailed_plots_clicked

    vertical_line = QtWidgets.QFrame()
    vertical_line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
    vertical_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
    hbox_main.addWidget(vertical_line)
    
    self.configuration_page.btn_load.clicked.connect(self.load_config)
    self.configuration_page.btn_save_as.clicked.connect(self.save_as_config)
    self.configuration_page.btn_save.clicked.connect(self.save_config)
    self.stacked_layout.addWidget(self.configuration_page)

    self.stacked_layout.addWidget(self.test_results_page)

    self.stacked_layout.addWidget(self.detailed_plots_page)

    hbox_main.addLayout(self.stacked_layout)

    self.setStatusBar(self.status_bar)
    self.status_bar.label_msg.setText("Test Started        Function: Negative Circuit Continuity        Pins: T01-1 & T01-11        Time Remaining: 1hr 30min")
    self.status_bar.progress_bar.setValue(30)