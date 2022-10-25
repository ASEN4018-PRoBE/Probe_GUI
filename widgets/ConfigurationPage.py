from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class ConfigurationPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

class ConfigurationElement(QtWidgets.QWidget):
    def __init__(self, title, test_list):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        vbox_main.addWidget(QtWidgets.QLabel(title))
        
        scroll = QtWidgets.QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setMaximumHeight(200)
        widget_scroll = QtWidgets.QWidget()
        scroll.setWidget(widget_scroll)
        vbox_scroll = QtWidgets.QVBoxLayout()
        widget_scroll.setLayout(vbox_scroll)
        vbox_main.addWidget(scroll)

        for d in test_list:
            vbox_scroll.addWidget(ConfigurationRow(d["Pin 1"],d["Pin 2"],d["Duration"],d["Pass Criteria"]))

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

        label_pass_criteria = QtWidgets.QLabel("Pass Criteria:")
        self.textbox_pass_criteria = QtWidgets.QLineEdit(pass_criteria)
        self.textbox_pass_criteria.setAlignment(Qt.AlignCenter)
        self.textbox_pass_criteria.setFixedWidth(100)

        hbox.addWidget(label_pin1)
        hbox.addWidget(self.textbox_pin1)
        hbox.addWidget(label_pin2)
        hbox.addWidget(self.textbox_pin2)
        hbox.addWidget(label_duration)
        hbox.addWidget(self.textbox_duration)
        hbox.addWidget(label_pass_criteria)
        hbox.addWidget(self.textbox_pass_criteria)