import matplotlib
matplotlib.use('Qt5Agg')

from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from .Fonts import font_regular, font_subtitle, font_title

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class DetailedPlotsPage(QtWidgets.QWidget):
    def __init__(self, test_config):
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
        self.label_func.setFont(font_regular)
        self.combo_func = QtWidgets.QComboBox()
        self.combo_func.setFont(font_regular)
        self.label_pin1 = QtWidgets.QLabel("Pin 1:")
        self.label_pin1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.label_pin1.setFont(font_regular)
        self.combo_pin1 = QtWidgets.QComboBox()
        self.combo_pin1.setFont(font_regular)
        self.label_pin2 = QtWidgets.QLabel("Pin 2:")
        self.label_pin2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.label_pin2.setFont(font_regular)
        self.combo_pin2 = QtWidgets.QComboBox()
        self.combo_pin2.setFont(font_regular)

        set_pin1 = set()
        set_pin2 = set()
        for key in test_config:
            if key!="Battery Name":
                self.combo_func.addItem(key)
                for d in test_config[key]["Pins"]:
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

        self.canvas = Canvas()

        vbox_main.addLayout(hbox_combo)
        vbox_main.addWidget(self.canvas)

        hbox_btn = QtWidgets.QHBoxLayout()
        self.btn_export = QtWidgets.QPushButton("Export")
        self.btn_export.setFont(font_regular)
        hbox_btn.addStretch(9)
        hbox_btn.addWidget(self.btn_export)
        vbox_main.addLayout(hbox_btn)

    def plot(self, x, y):
        self.canvas.axes.cla()
        self.canvas.axes.grid()
        self.canvas.axes.plot(x,y)
        self.canvas.draw()

class Canvas(FigureCanvasQTAgg):
    def __init__(self, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        self.axes = fig.add_subplot(111)
        self.axes.grid()
        super(Canvas, self).__init__(fig)
