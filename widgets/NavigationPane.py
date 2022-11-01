import sys

from PyQt5.QtCore import Qt
from .Fonts import font_regular

from PyQt5 import QtWidgets 


class NavigationPane(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)
        vbox_main.setObjectName("vbox_main")
        self.setFixedWidth(200)

        self.btn_configuration = QtWidgets.QLabel("Configuration")
        self.btn_configuration.setFixedHeight(80)
        self.btn_configuration.setFont(font_regular)
        self.btn_test_results = QtWidgets.QLabel("Test Results")
        self.btn_test_results.setFixedHeight(80)
        self.btn_test_results.setFont(font_regular)
        self.btn_detailed_plots = QtWidgets.QLabel("Detailed Plots")
        self.btn_detailed_plots.setFixedHeight(80)
        self.btn_detailed_plots.setFont(font_regular)
        self.btn_start = QtWidgets.QPushButton("Start")
        self.btn_start.setFont(font_regular)
        self.btn_pause_resume = QtWidgets.QPushButton("Pause")
        self.btn_pause_resume.setFont(font_regular)
        self.btn_stop = QtWidgets.QPushButton("Stop")
        self.btn_stop.setFont(font_regular)
        
        vbox_main.addWidget(self.btn_configuration)
        vbox_main.addWidget(self.btn_test_results)
        vbox_main.addWidget(self.btn_detailed_plots)
        vbox_main.addStretch(1)
        vbox_main.addWidget(self.btn_start)
        vbox_main.addWidget(self.btn_pause_resume)
        vbox_main.addWidget(self.btn_stop)

        self.setStyleSheet('''
            QLabel{
                font-size: 20px;
                font-weight: 400;
                text-align:left;
            }
            QLabel:hover{
                color: rgb(150,150,150)
            }
        ''')

