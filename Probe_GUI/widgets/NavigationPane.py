import sys

from PyQt5.QtCore import Qt
from .Fonts import font_title, font_subtitle

from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QVBoxLayout 
from PyQt5.QtWidgets import QPushButton


class NavigationPane(QtWidgets.QWidget):
    def __init__(self, test_template):
        super().__init__()
        vbox_main = QtWidgets.QVBoxLayout()
        self.setLayout(vbox_main)

        title = QtWidgets.QLabel("Navigation Pane")
        title.setFont(font_title)
        vbox_main.addWidget(title)
        

        #Create QV Box Layout
        layout = QVBoxLayout()
        # Add widgets to the layout
        vbox_main.addWidget(QPushButton("Configuration"))
        vbox_main.addWidget(QPushButton("Test Results"))
        vbox_main.addWidget(QPushButton("Detailed Plots"))
        vbox_main.addWidget(QPushButton("Start"))
        vbox_main.addWidget(QPushButton("Pause / Resume"))
        vbox_main.addWidget(QPushButton("Stop"))
        vbox_main.addWidget(QPushButton("Progress Bar"))

        
  