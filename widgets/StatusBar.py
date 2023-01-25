from PyQt6 import QtWidgets
import qdarktheme

from .Fonts import font_regular, font_subtitle, font_title

class StatusBar(QtWidgets.QStatusBar):
    def __init__(self):
        super().__init__()
        space = QtWidgets.QWidget()
        space.setFixedWidth(15)
        self.addWidget(space)

        self.label_msg = QtWidgets.QLabel("test not started")
        self.label_msg.setFont(font_regular)
        self.label_msg.setFixedHeight(30)
        self.addWidget(self.label_msg)

        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setFixedSize(200,20)
        self.progress_bar.setValue(0)
        self.addPermanentWidget(self.progress_bar)

        space2 = QtWidgets.QWidget()
        space2.setFixedWidth(15)
        self.addPermanentWidget(space2)

        self.setStyleSheet('''
            QProgressBar{
                border: 1px solid gray;
            }
        ''')

    def set_message(self, started:bool, test_function, pin1, pin2):
        b = " "*10
        text_started = "Test Not Running"
        if started: text_started = "Test Running"
        text = f"{text_started}{b}Testing: {test_function} @ {pin1} & {pin2}"
        self.label_msg.setText(text)