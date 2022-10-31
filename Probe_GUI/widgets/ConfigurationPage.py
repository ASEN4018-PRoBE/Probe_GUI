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

        for key in test_template:
            if key!="Battery Name":
                vbox_scroll.addWidget(ConfigurationElement(key,test_template[key]["Duration"],test_template[key]["Pass Criteria"],test_template[key]["Pins"]))

        hbox_btn = QtWidgets.QHBoxLayout()
        vbox_main.addLayout(hbox_btn)
        hbox_btn.addStretch(7)
        self.btn_load = QtWidgets.QPushButton("Load")
        hbox_btn.addWidget(self.btn_load,1)
        self.btn_save_as = QtWidgets.QPushButton("Save As...")
        hbox_btn.addWidget(self.btn_save_as,1)
        self.btn_save = QtWidgets.QPushButton("Save")
        hbox_btn.addWidget(self.btn_save,1)

# A block of rows make up Configuration Element for a specific test
# title: the test function name, i.e.: "Continuity", "Isolation" ...
# pins_list: a list of dictonaries containing pins, duration and pass criteria
# duration: duration as string indicating how long to hold on pins in seconds
# pass_criteria: "[lower, upper] units" as string for pass/fail determination
class ConfigurationElement(QtWidgets.QWidget):
    def __init__(self, title, duration, pass_criteria, pins_list):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        hbox_title = QtWidgets.QHBoxLayout()
        title = QtWidgets.QLabel(title)
        title.setFont(font_subtitle)
        label_duration = QtWidgets.QLabel("Pin Hold Duration:")
        self.textbox_duration = QtWidgets.QLineEdit(duration)
        self.textbox_duration.setAlignment(Qt.AlignCenter)
        self.textbox_duration.setFixedWidth(50)
        label_pass_criteria = QtWidgets.QLabel("Pass Criteria:")
        self.textbox_pass_criteria = QtWidgets.QLineEdit(pass_criteria)
        self.textbox_pass_criteria.setAlignment(Qt.AlignCenter)
        self.textbox_pass_criteria.setFixedWidth(150)

        hbox_title.addWidget(title)
        hbox_title.addWidget(label_duration)
        hbox_title.addWidget(self.textbox_duration)
        hbox_title.addWidget(label_pass_criteria)
        hbox_title.addWidget(self.textbox_pass_criteria)
        hbox_title.addStretch(6)
        vbox_main.addLayout(hbox_title)
        
        scroll = QtWidgets.QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(min(80*len(pins_list),200))
        widget_scroll = QtWidgets.QWidget()
        scroll.setWidget(widget_scroll)
        vbox_scroll = QtWidgets.QVBoxLayout()
        widget_scroll.setLayout(vbox_scroll)
        vbox_main.addWidget(scroll)

        self.configuration_rows = []

        for i in range(0,len(pins_list),2):
            hbox_row = QtWidgets.QHBoxLayout() # one row contains two pin combinations
            self.configuration_rows.append(ConfigurationRow(pins_list[i]["Pin 1"],pins_list[i]["Pin 2"]))
            hbox_row.addWidget(self.configuration_rows[-1],5)
            if i+1!=len(pins_list):
                vertical_line = QtWidgets.QFrame()
                vertical_line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
                vertical_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                vertical_line.setFixedHeight(30)
                hbox_row.addWidget(vertical_line,1)
                self.configuration_rows.append(ConfigurationRow(pins_list[i+1]["Pin 1"],pins_list[i+1]["Pin 2"]))
                hbox_row.addWidget(self.configuration_rows[-1],5)
            else:
                hbox_row.addStretch(5)
            
            vbox_scroll.addLayout(hbox_row)

# A basic row in Configuration Page
# pin1: pin1 as string in test sequence
# pin2: pin2 as string in test sequence
class ConfigurationRow(QtWidgets.QWidget):
    def __init__(self, pin1, pin2):
        super().__init__()
        hbox = QtWidgets.QHBoxLayout()
        self.setLayout(hbox)
        label_pin1 = QtWidgets.QLabel("Pin 1:")
        self.textbox_pin1 = QtWidgets.QLineEdit(pin1)
        self.textbox_pin1.setAlignment(Qt.AlignCenter)

        label_pin2 = QtWidgets.QLabel("Pin 2:")
        self.textbox_pin2 = QtWidgets.QLineEdit(pin2)
        self.textbox_pin2.setAlignment(Qt.AlignCenter)

        hbox.addWidget(label_pin1)
        hbox.addWidget(self.textbox_pin1)
        hbox.addWidget(label_pin2)
        hbox.addWidget(self.textbox_pin2)