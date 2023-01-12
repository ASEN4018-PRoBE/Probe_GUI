from PyQt6 import QtWidgets
from .Fonts import font_title

class HelpAboutPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        title = QtWidgets.QLabel("Help & About")
        title.setFont(font_title)
        self.layout().addWidget(title)

        self.text_browser = QtWidgets.QTextBrowser()
        self.layout().addWidget(self.text_browser)
        with open("help_about.html") as f: content = f.read()
        self.text_browser.append(content)
