from PyQt6.QtGui import QFont

# mac
name = "Arial"
font_title = QFont(name, 20, QFont.Weight.Bold)
font_subtitle = QFont(name, 16, QFont.Weight.DemiBold)
font_regular = QFont(name, 13, QFont.Weight.Normal)
font_regular_bold = QFont(name, 13, QFont.Weight.Bold)

# windows
# font_title = QFont("Calibri", 18, QFont.Weight.Bold)
# font_subtitle = QFont("Calibri", 14, QFont.Weight.DemiBold)
# font_regular = QFont("Calibri", 10, QFont.Weight.Normal)
# font_regular_bold = QFont("Calibri", 10, QFont.Weight.Bold)