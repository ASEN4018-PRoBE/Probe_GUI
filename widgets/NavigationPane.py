import sys

from PyQt5.QtCore import Qt
from .Fonts import font_title, font_subtitle

from PyQt5 import QtWidgets 


class NavigationPane(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)
        self.setFixedWidth(200)

        self.btn_configuration = QtWidgets.QPushButton("Configuration")
        self.btn_test_results = QtWidgets.QPushButton("Test Results")
        self.btn_detailed_plots = QtWidgets.QPushButton("Detailed Plots")
        self.btn_start = QtWidgets.QPushButton("Start")
        self.btn_pause_resume = QtWidgets.QPushButton("Pause/Resume")
        self.btn_stop = QtWidgets.QPushButton("Stop")
        self.progess_bar = QtWidgets.QProgressBar()
        
        vbox_main.addStretch(1)
        vbox_main.addWidget(self.btn_configuration)
        vbox_main.addStretch(1)
        vbox_main.addWidget(self.btn_test_results)
        vbox_main.addStretch(1)
        vbox_main.addWidget(self.btn_detailed_plots)
        vbox_main.addStretch(7)
        vbox_main.addWidget(self.btn_start)
        vbox_main.addWidget(self.btn_pause_resume)
        vbox_main.addWidget(self.btn_stop)
        vbox_main.addWidget(self.progess_bar)
        vbox_main.addStretch(1)

        self.setStyleSheet('''
            QPushButton{
                border:none;
                font-size:20px;
                font-weight:400;
                text-align:left;
            }
            QPushButton#left_button:hover{
                font-weight:600;
                background:rgb(220,220,220);
                border-left:5px solid blue;
            }
            QWidget#left_widget{
                background:rgb(220,220,220);
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')
