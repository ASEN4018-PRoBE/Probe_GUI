from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

from .Fonts import font_title, font_subtitle, font_regular, font_regular_bold

# Configuration Page for display in MainWindow
# test_config: dictionary for test setup info, see test_template/test_template.json
class ConfigurationPage(QtWidgets.QWidget):
    def __init__(self, test_config):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        title = QtWidgets.QLabel(test_config["Battery Name"]+" Configuration")
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

        for key in test_config:
            if key!="Battery Name":
                vbox_scroll.addWidget(ConfigurationElement(key,test_config[key]))

        hbox_btn = QtWidgets.QHBoxLayout()
        vbox_main.addLayout(hbox_btn)
        hbox_btn.addStretch(7)
        self.btn_load = QtWidgets.QPushButton("Load")
        self.btn_load.setFont(font_regular)
        hbox_btn.addWidget(self.btn_load,1)
        self.btn_save_as = QtWidgets.QPushButton("Save As...")
        self.btn_save_as.setFont(font_regular)
        hbox_btn.addWidget(self.btn_save_as,1)
        self.btn_save = QtWidgets.QPushButton("Save")
        self.btn_save.setFont(font_regular)
        hbox_btn.addWidget(self.btn_save,1)

# A block of rows make up Configuration Element for a specific test
# title: the test function name, i.e.: "Continuity", "Isolation" ...
# function_dict: dictionary for details for the test function
class ConfigurationElement(QtWidgets.QWidget):
    def __init__(self, title, function_dict):
        super().__init__()
        self.function_dict = function_dict # reference to test function configuration in test_template 
        pins_list = function_dict["Pins"]

        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        hbox_title = QtWidgets.QHBoxLayout()
        label_title = QtWidgets.QLabel(title)
        label_title.setFont(font_subtitle)
        label_duration = QtWidgets.QLabel("Pin Hold Duration [s]:")
        label_duration.setFont(font_regular)
        textbox_duration = QtWidgets.QLineEdit(self.function_dict["Duration"])
        textbox_duration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        textbox_duration.setFixedWidth(50)
        textbox_duration.setValidator(QRegularExpressionValidator(QRegularExpression("^[1-9]\d{1,2}$")))
        textbox_duration.textChanged.connect(lambda: self.function_dict.update({"Duration":textbox_duration.text()}))
        textbox_duration.setFont(font_regular)
        label_pass_criteria = QtWidgets.QLabel("Pass Criteria:")
        label_pass_criteria.setFont(font_regular)
        textbox_pass_criteria = QtWidgets.QLineEdit(self.function_dict["Pass Criteria"])
        textbox_pass_criteria.setAlignment(Qt.AlignmentFlag.AlignCenter)
        textbox_pass_criteria.setFixedWidth(150)
        textbox_pass_criteria.textChanged.connect(lambda: self.function_dict.update({"Pass Criteria":textbox_pass_criteria.text()}))
        # textbox_pass_criteria.setValidator(QRegularExpressionValidator(QRegularExpression("^\[\d+\.?\d* \d+\.?\d*\] [A-Za-z]+$")))
        textbox_pass_criteria.setFont(font_regular)

        hbox_title.addWidget(label_title)
        hbox_title.addWidget(label_duration)
        hbox_title.addWidget(textbox_duration)
        hbox_title.addWidget(label_pass_criteria)
        hbox_title.addWidget(textbox_pass_criteria)
        hbox_title.addStretch(6)
        vbox_main.addLayout(hbox_title)
        
        # scroll = QtWidgets.QScrollArea()
        # scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # scroll.setWidgetResizable(True)
        # scroll.setFixedHeight(min(80*len(pins_list),200))
        # widget_scroll = QtWidgets.QWidget()
        # scroll.setWidget(widget_scroll)
        # grid_scroll = QtWidgets.QGridLayout()
        # widget_scroll.setLayout(grid_scroll)
        # vbox_main.addWidget(scroll)

        grid_scroll = QtWidgets.QGridLayout()
        frame_grid = QtWidgets.QFrame()
        frame_grid.setLayout(grid_scroll)
        frame_grid.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel|QtWidgets.QFrame.Shadow.Plain)
        vbox_main.addWidget(frame_grid)

        for i in range(11): grid_scroll.setColumnStretch(i,1)

        self.configuration_rows = []

        for i in range(0,len(pins_list),2):
            self.configuration_rows.append(ConfigurationRow(i+1,pins_list[i]))
            grid_scroll.addWidget(self.configuration_rows[-1],i//2,0,1,5)
            vertical_line = QtWidgets.QFrame()
            vertical_line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
            vertical_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
            vertical_line.setFixedHeight(30)
            grid_scroll.addWidget(vertical_line,i//2,5,1,1)
            if i+1!=len(pins_list):
                self.configuration_rows.append(ConfigurationRow(i+2,pins_list[i+1]))
                grid_scroll.addWidget(self.configuration_rows[-1],i//2,6,1,5)
            else:
                grid_scroll.addWidget(QtWidgets.QWidget(),i//2,6,1,5)


# A basic row in Configuration Page
# pins: dictionary of pin combination in test_template
class ConfigurationRow(QtWidgets.QWidget):
    def __init__(self, index, pins):
        super().__init__()
        hbox = QtWidgets.QHBoxLayout()
        self.setLayout(hbox)
        label_index = QtWidgets.QLabel(str(index)+".")
        label_index.setFont(font_regular_bold)
        label_pin1 = QtWidgets.QLabel("Pin 1:")
        label_pin1.setFont(font_regular)
        textbox_pin1 = QtWidgets.QLineEdit(pins["Pin 1"])
        textbox_pin1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        textbox_pin1.textChanged.connect(lambda: pins.update({"Pin 1":textbox_pin1.text()}))
        textbox_pin1.setFont(font_regular)

        label_pin2 = QtWidgets.QLabel("Pin 2:")
        label_pin2.setFont(font_regular)
        textbox_pin2 = QtWidgets.QLineEdit(pins["Pin 2"])
        textbox_pin2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        textbox_pin2.textChanged.connect(lambda: pins.update({"Pin 2":textbox_pin2.text()}))
        textbox_pin2.setFont(font_regular)

        hbox.addWidget(label_index)
        hbox.addWidget(label_pin1)
        hbox.addWidget(textbox_pin1)
        hbox.addWidget(label_pin2)
        hbox.addWidget(textbox_pin2)