from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from .Fonts import font_title, font_subtitle, font_regular

class TestResultsPage(QtWidgets.QWidget):
    def __init__(self, test_template):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        title = QtWidgets.QLabel("Test Results "+test_template["Battery Name"])
        title.setFont(font_title)
        vbox_main.addWidget(title)

        scroll = QtWidgets.QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        widget_scroll = QtWidgets.QWidget()
        scroll.setWidget(widget_scroll)
        vbox_scroll = QtWidgets.QVBoxLayout()
        widget_scroll.setLayout(vbox_scroll)
        vbox_main.addWidget(scroll)

        self.element_dict = dict()
        for key in test_template:
            if key!="Battery Name":
                self.element_dict[key] = TestResultsElement(key, test_template[key]["Pass Criteria"])
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
        hbox_title.addWidget(title)
        hbox_title.addWidget(label_pass_criteria)
        hbox_title.addStretch(6)
        vbox_main.addLayout(hbox_title)
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        widget_scroll = QtWidgets.QWidget()
        self.scroll_area.setWidget(widget_scroll)
        self.vbox_scroll = QtWidgets.QVBoxLayout()
        widget_scroll.setLayout(self.vbox_scroll)
        vbox_main.addWidget(self.scroll_area)

        self.test_result_rows = []
    
    def append_test_result(self, pin1, pin2, measurement, pass_fail):
        row = TestResultsRow(pin1, pin2, measurement, pass_fail)
        self.test_result_rows.append(row)
        self.scroll_area.setFixedHeight(min(80*len(self.test_result_rows),200))
        self.vbox_scroll.addWidget(row)


# pin1: pin1 as string in test sequence
# pin2: pin2 as string in test sequence
# measurement: measurement result as string from DMM
# pass_fail: pass or fail as bool
class TestResultsRow(QtWidgets.QWidget):
    def __init__(self, pin1, pin2, measurement, pass_fail):
        super().__init__()
        hbox = QtWidgets.QHBoxLayout()
        self.setLayout(hbox)

        label_pin1 = QtWidgets.QLabel("Pin 1: "+pin1)
        label_pin1.setAlignment(Qt.AlignCenter)
        label_pin1.setFont(font_regular)
        label_pin2 = QtWidgets.QLabel("Pin 2: "+pin2)
        label_pin2.setAlignment(Qt.AlignCenter)
        label_pin2.setFont(font_regular)
        label_measurement = QtWidgets.QLabel("Measurement: "+measurement)
        label_measurement.setAlignment(Qt.AlignCenter)
        label_measurement.setFont(font_regular)
        sign_pass_fail = "✅" if pass_fail else "❌"
        label_pass_fail = QtWidgets.QLabel("Pass: "+sign_pass_fail)
        label_pass_fail.setAlignment(Qt.AlignCenter)
        label_pass_fail.setFont(font_regular)

        hbox.addWidget(label_pin1,2)
        hbox.addWidget(label_pin2,2)
        hbox.addWidget(label_measurement,3)
        hbox.addWidget(label_pass_fail,2)