from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from .Fonts import font_regular, font_subtitle, font_title

class DetailedPlotsPage(QtWidgets.QWidget):
    def __init__(self, test_template):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        title = QtWidgets.QLabel("Detailed Plots")
        title.setFont(font_title)
        vbox_main.addWidget(title)
        vbox_main.addStretch(1)

        hbox_combo = QtWidgets.QHBoxLayout()

        self.label_func = QtWidgets.QLabel("Function:")
        self.label_func.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.combo_func = QtWidgets.QComboBox()
        self.label_pin1 = QtWidgets.QLabel("Pin 1:")
        self.label_pin1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.combo_pin1 = QtWidgets.QComboBox()
        self.label_pin2 = QtWidgets.QLabel("Pin 2:")
        self.label_pin2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.combo_pin2 = QtWidgets.QComboBox()

        set_pin1 = set()
        set_pin2 = set()
        for key in test_template:
            if key!="Battery Name":
                self.combo_func.addItem(key)
                for d in test_template[key]["Pins"]:
                    set_pin1.add(d["Pin 1"])
                    set_pin2.add(d["Pin 2"])
        self.combo_pin1.addItems(sorted(list(set_pin1)))
        self.combo_pin2.addItems(sorted(list(set_pin2)))

        hbox_combo.addWidget(self.label_func,1)
        hbox_combo.addWidget(self.combo_func,3)
        hbox_combo.addWidget(self.label_pin1,1)
        hbox_combo.addWidget(self.combo_pin1,2)
        hbox_combo.addWidget(self.label_pin2,1)
        hbox_combo.addWidget(self.combo_pin2,2)

        label_plot = QtWidgets.QLabel()
        label_plot.setPixmap(QtGui.QPixmap("./plot.png"))
        label_plot.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox_main.addLayout(hbox_combo)
        vbox_main.addWidget(label_plot)
        vbox_main.addStretch(1)