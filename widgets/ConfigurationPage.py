from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from .Fonts import font_title, font_subtitle

# Configuration Page for display in MainWindow
# test_template: dictionary for test setup info, see test_template/test_template.json
class ConfigurationPage(QtWidgets.QWidget):
    def __init__(self, test_template):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        title = QtWidgets.QLabel(test_template["Battery Name"])
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

        self.rows = []

        for key in test_template:
            if key!="Battery Name":
                self.rows.append(ConfigurationElement(key,test_template[key]))
                vbox_scroll.addWidget(self.rows[-1])

        hbox_btn = QtWidgets.QHBoxLayout()
        vbox_main.addLayout(hbox_btn)
        hbox_btn.addStretch(8)
        self.btn_load = QtWidgets.QPushButton("Load")
        hbox_btn.addWidget(self.btn_load,1)
        self.btn_save = QtWidgets.QPushButton("Save")
        hbox_btn.addWidget(self.btn_save,1)

# A block of rows make up Configuration Element for a specific test
# title: the test function name, i.e.: "Continuity", "Isolation"...
# test_list: a list of dictonaries containing pins, duration and pass criteria
class ConfigurationElement(QtWidgets.QWidget):
    def __init__(self, title, test_list):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        title = QtWidgets.QLabel(title)
        title.setFont(font_subtitle)
        vbox_main.addWidget(title)
        
        scroll = QtWidgets.QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(min(80*len(test_list),200))
        widget_scroll = QtWidgets.QWidget()
        scroll.setWidget(widget_scroll)
        vbox_scroll = QtWidgets.QVBoxLayout()
        widget_scroll.setLayout(vbox_scroll)
        vbox_main.addWidget(scroll)

        for d in test_list:
            vbox_scroll.addWidget(ConfigurationRow(d["Pin 1"],d["Pin 2"],d["Duration"],d["Pass Criteria"]))

# A basic row in Configuration Page
# pin1: pin1 as string in test sequence
# pin2: pin2 as string in test sequence
# duration: duration as string indicating how long to hold on pins in seconds
# pass_criteria: "[low, upper] units" as string for pass/fail determination
class ConfigurationRow(QtWidgets.QWidget):
    def __init__(self, pin1=None, pin2=None, duration=None, pass_criteria=None):
        super().__init__()
        hbox = QtWidgets.QHBoxLayout()
        self.setLayout(hbox)
        label_pin1 = QtWidgets.QLabel("Pin 1:")
        self.textbox_pin1 = QtWidgets.QLineEdit(pin1)
        self.textbox_pin1.setAlignment(Qt.AlignCenter)
        self.textbox_pin1.setFixedWidth(60)

        label_pin2 = QtWidgets.QLabel("Pin 2:")
        self.textbox_pin2 = QtWidgets.QLineEdit(pin2)
        self.textbox_pin2.setAlignment(Qt.AlignCenter)
        self.textbox_pin2.setFixedWidth(60)

        label_duration = QtWidgets.QLabel("Duration:")
        self.textbox_duration = QtWidgets.QLineEdit(duration)
        self.textbox_duration.setAlignment(Qt.AlignCenter)
        self.textbox_duration.setFixedWidth(50)

        label_pass_criteria = QtWidgets.QLabel("Pass Criteria:")
        self.textbox_pass_criteria = QtWidgets.QLineEdit(pass_criteria)
        self.textbox_pass_criteria.setAlignment(Qt.AlignCenter)
        self.textbox_pass_criteria.setFixedWidth(150)

        hbox.addWidget(label_pin1)
        hbox.addWidget(self.textbox_pin1)
        hbox.addWidget(label_pin2)
        hbox.addWidget(self.textbox_pin2)
        hbox.addWidget(label_duration)
        hbox.addWidget(self.textbox_duration)
        hbox.addWidget(label_pass_criteria)
        hbox.addWidget(self.textbox_pass_criteria)