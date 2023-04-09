from PyQt6 import QtWidgets
import qdarktheme

from .Fonts import font_regular, font_subtitle, font_title

class StatusBar(QtWidgets.QStatusBar):
    def __init__(self):
        super().__init__()
        space = QtWidgets.QWidget()
        space.setFixedWidth(15)
        self.addWidget(space)

        self.label_msg = QtWidgets.QLabel("Test Not Started")
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

    def set_message(self, msg=None, test_function="n/a", pin1="n/a", pin2="n/a"):
        b = " "*10
        text_started = msg
        text = f"{text_started}{b}Testing: {test_function} @ {pin1} & {pin2}"
        self.label_msg.setText(text)