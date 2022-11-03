from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from .Fonts import font_regular

class NavigationPane(QtWidgets.QWidget):
    def __init__(self, light):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)
        vbox_main.setObjectName("vbox_main")
        self.setFixedWidth(200)

        self.btn_configuration = QtWidgets.QLabel("Configuration")
        self.btn_configuration.setFixedHeight(80)
        self.btn_configuration.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)
        self.btn_configuration.setFont(font_regular)
        self.btn_test_results = QtWidgets.QLabel("Test Results")
        self.btn_test_results.setFixedHeight(80)
        self.btn_test_results.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)
        self.btn_test_results.setFont(font_regular)
        self.btn_detailed_plots = QtWidgets.QLabel("Detailed Plots")
        self.btn_detailed_plots.setFixedHeight(80)
        self.btn_detailed_plots.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)
        self.btn_detailed_plots.setFont(font_regular)
        
        vbox_main.addWidget(self.btn_configuration)
        vbox_main.addWidget(self.btn_test_results)
        vbox_main.addWidget(self.btn_detailed_plots)
        vbox_main.addStretch(1)

        hbox_btn = QtWidgets.QHBoxLayout()
        self.btn_start = QtWidgets.QPushButton("▶️")
        self.btn_pause_resume = QtWidgets.QPushButton("⏯")
        self.btn_stop = QtWidgets.QPushButton("⏹")
        self.btn_stop.setFont(font_regular)
        hbox_btn.addWidget(self.btn_start)
        hbox_btn.addWidget(self.btn_pause_resume)
        hbox_btn.addWidget(self.btn_stop)
        vbox_main.addLayout(hbox_btn)
        self.btn_start.setFixedHeight(50)
        self.btn_pause_resume.setFixedHeight(50)
        self.btn_stop.setFixedHeight(50)

        self.setStyleSheet('''
            QPushButton{{
                font-size: 25px;
                border: 1px solid gray;
            }}
            QLabel{{
                font-size: 20px;
                font-weight: 400;
                text-align: center;
            }}
            QLabel::hover{{
                background: rgb({0},{1},{2})
            }}
        '''.format(light.red(),light.green(),light.blue()))

    def recolor(self, index, base, light):
        self.btn_configuration.setStyleSheet("QLabel{{background: rgb({0},{1},{2}}})".format(base.red(),base.green(),base.blue()))
        self.btn_test_results.setStyleSheet("QLabel{{background: rgb({0},{1},{2}}})".format(base.red(),base.green(),base.blue()))
        self.btn_detailed_plots.setStyleSheet("QLabel{{background: rgb({0},{1},{2}}})".format(base.red(),base.green(),base.blue()))
        if index==0:
            self.btn_configuration.setStyleSheet("background: rgb({0},{1},{2})".format(light.red(),light.green(),light.blue()))
        elif index==1:
            self.btn_test_results.setStyleSheet("background: rgb({0},{1},{2})".format(light.red(),light.green(),light.blue()))
        elif index==2:
            self.btn_detailed_plots.setStyleSheet("background: rgb({0},{1},{2})".format(light.red(),light.green(),light.blue()))
