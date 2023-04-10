import matplotlib
from PyQt6 import QtWidgets
from .Fonts import font_regular, font_subtitle, font_title
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import global_vars, widgets.FlowLayout as FlowLayout

plt.style.use('ggplot')

class DetailedPlotsPage(QtWidgets.QWidget):
    def __init__(self, test_config):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        title = QtWidgets.QLabel("Detailed Plots")
        title.setFont(font_title)
        vbox_main.addWidget(title)

        vbox_main.addStretch()

        frame = QtWidgets.QFrame()
        frame.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel|QtWidgets.QFrame.Shadow.Plain)
        frame.setLayout(QtWidgets.QVBoxLayout())
        vbox_main.addWidget(frame)

        flow_radio = FlowLayout.FlowLayout()
        self.radio_btns_dict = dict()
        for test_function in global_vars.test_functions:
            radio_btn = QtWidgets.QRadioButton(test_function)
            flow_radio.addWidget(radio_btn)
            self.radio_btns_dict[test_function] = radio_btn
        frame.layout().addLayout(flow_radio)

        hbox_combo = QtWidgets.QHBoxLayout()
        self.combo_pin1 = QtWidgets.QComboBox()
        self.combo_pin1.setFixedWidth(150)
        self.combo_pin1.setPlaceholderText("Select Pin 1")
        self.combo_pin2 = QtWidgets.QComboBox()
        self.combo_pin2.setFixedWidth(150)
        self.combo_pin2.setPlaceholderText("Selct Pin 2")
        hbox_combo.addStretch()
        hbox_combo.addWidget(self.combo_pin1)
        hbox_combo.addWidget(self.combo_pin2)
        frame.layout().addLayout(hbox_combo)

        matplotlib.use('Qt5Agg')
        self.canvas = Canvas()
        frame.layout().addWidget(self.canvas)

        hbox_btn = QtWidgets.QHBoxLayout()
        self.btn_export = QtWidgets.QPushButton("Export")
        self.btn_export.setFont(font_regular)
        hbox_btn.addStretch(9)
        hbox_btn.addWidget(self.btn_export)
        frame.layout().addLayout(hbox_btn)

        vbox_main.addStretch()

    def plot(self, x, y):
        self.canvas.axes.grid()
        self.canvas.axes.set_xlabel('time', fontsize=10)
        self.canvas.axes.set_ylabel('reading', fontsize=10)
        self.canvas.axes.tick_params(axis='both', which='major', labelsize=8)
        self.canvas.axes.plot(x,y)
        self.canvas.draw()

    def plot_pin_readings(self, pin_readings):
        self.canvas.axes.cla()
        plt.grid()
        self.canvas.axes.set_xlabel('time', fontsize=10)
        self.canvas.axes.set_ylabel('reading', fontsize=10)
        self.canvas.axes.tick_params(axis='both', which='major', labelsize=8)
        for pin_reading in pin_readings:
            self.canvas.axes.plot(pin_reading.time, pin_reading.reading)
        self.canvas.draw()

    def clear(self):
        self.canvas.axes.cla()

class Canvas(FigureCanvasQTAgg):
    def __init__(self, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        self.axes = fig.add_subplot(1,1,1)
        super(Canvas, self).__init__(fig)
