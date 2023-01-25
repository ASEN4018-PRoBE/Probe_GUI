import random

from PyQt6 import QtWidgets, QtSvgWidgets
from PyQt6.QtCore import Qt

from .Fonts import font_title, font_subtitle, font_regular

class TestResultsPage(QtWidgets.QWidget):
    def __init__(self, test_config):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        title = QtWidgets.QLabel("Test Results")
        title.setFont(font_title)
        vbox_main.addWidget(title)

        scroll = QtWidgets.QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        widget_scroll = QtWidgets.QWidget()
        scroll.setWidget(widget_scroll)
        vbox_scroll = QtWidgets.QVBoxLayout()
        widget_scroll.setLayout(vbox_scroll)
        vbox_main.addWidget(scroll)

        self.element_dict = dict()
        for key in test_config:
            if key!="Battery Name":
                self.element_dict[key] = TestResultsElement(key, test_config[key]["Pass Criteria"])
                vbox_scroll.addWidget(self.element_dict[key])

        hbox_btn = QtWidgets.QHBoxLayout()
        self.btn_export = QtWidgets.QPushButton("Export")
        self.btn_export.setFont(font_regular)
        hbox_btn.addStretch(9)
        hbox_btn.addWidget(self.btn_export)
        vbox_main.addLayout(hbox_btn)

class TestResultsElement(QtWidgets.QWidget):
    def __init__(self, title, pass_criteria):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        hbox_title = QtWidgets.QHBoxLayout()
        title = QtWidgets.QLabel(title)
        title.setFont(font_subtitle)
        label_pass_criteria = QtWidgets.QLabel("Pass Criteria: "+pass_criteria)
        label_pass_criteria.setFont(font_regular)
        hbox_title.addWidget(title)
        hbox_title.addWidget(label_pass_criteria)
        hbox_title.addStretch(6)
        vbox_main.addLayout(hbox_title)

        self.grid = QtWidgets.QGridLayout()
        frame_grid = QtWidgets.QFrame()
        frame_grid.setLayout(self.grid)
        frame_grid.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel|QtWidgets.QFrame.Shadow.Plain)
        vbox_main.addWidget(frame_grid)

        for i in range(11): self.grid.setColumnStretch(i,1)

        self.test_result_rows = []
    
    def append_test_result(self, pin1, pin2, measurement, pass_fail):
        row = TestResultsRow(pin1, pin2, measurement, pass_fail)
        l = len(self.test_result_rows)
        self.test_result_rows.append(row)
        if l%2==0:
            self.grid.addWidget(row,l//2,0,1,5)
            self.grid.addWidget(QtWidgets.QWidget(),l//2,6,1,5)
        else:
            vertical_line = QtWidgets.QFrame()
            vertical_line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
            vertical_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
            vertical_line.setFixedHeight(30)
            self.grid.addWidget(vertical_line,l//2,5,1,1)
            self.grid.addWidget(row,l//2,6,1,5)

# pin1: pin1 as string in test sequence
# pin2: pin2 as string in test sequence
# measurement: measurement result as string from DMM
# pass_fail: pass or fail as bool
class TestResultsRow(QtWidgets.QWidget):
    def __init__(self, pin1, pin2, measurement, pass_fail:bool):
        super().__init__()
        hbox = QtWidgets.QHBoxLayout()
        self.setLayout(hbox)
        self.max_length_measurement = 5

        label_pin1 = QtWidgets.QLabel("Pin 1: "+pin1)
        label_pin1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_pin1.setFont(font_regular)
        label_pin2 = QtWidgets.QLabel("Pin 2: "+pin2)
        label_pin2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_pin2.setFont(font_regular)
        label_measurement = QtWidgets.QLabel(measurement)
        label_measurement.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_measurement.setFont(font_regular)
        if pass_fail:
            label_pass_fail_svg = QtSvgWidgets.QSvgWidget("images/checkmark.square.fill.svg")
        else:
            label_pass_fail_svg = QtSvgWidgets.QSvgWidget("images/xmark.square.fill.svg")
        label_pass_fail_svg.setFixedSize(15,15)
        hbox.addStretch(1)
        hbox.addWidget(label_pin1,2)
        hbox.addStretch(1)
        hbox.addWidget(label_pin2,2)
        hbox.addStretch(1)
        hbox.addWidget(label_measurement,2)
        hbox.addStretch(1)
        hbox.addWidget(label_pass_fail_svg,2)
        hbox.addStretch(1)