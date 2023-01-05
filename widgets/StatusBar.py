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

        self.theme_light = False
        self.btn_theme = QtWidgets.QPushButton("🔆")
        self.btn_theme.setFixedHeight(26)
        self.btn_theme.clicked.connect(self.btn_theme_clicked)
        #self.addPermanentWidget(self.btn_theme)

        self.setStyleSheet('''
            QProgressBar{
                border: 1px solid gray;
            }
        ''')
    
    def btn_theme_clicked(self):
        if not self.theme_light:
            QtWidgets.QApplication.instance().setStyleSheet(qdarktheme.load_stylesheet("light"))
            self.theme_light = True
        else:
            QtWidgets.QApplication.instance().setStyleSheet(qdarktheme.load_stylesheet("dark"))
            self.theme_light = False