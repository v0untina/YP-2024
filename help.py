from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QWidget, QScrollArea
from PyQt6.QtCore import Qt
import sys

class helpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 300,500,560)
        grid = QGridLayout()
        self.setFixedSize(500, 560)
        self.setLayout(grid)
        words = list()
        with open('help.txt', 'r', encoding="utf-8") as f:
            words = list(str(f.read()))
        self.setWindowTitle("Справка")

        label = QLabel(''.join(map(str, words)))
        label.setWordWrap(True)
        label.setStyleSheet("""
            QLabel { 
                font-family: 'Arial Black', sans-serif; 
                font-size: 14px; 
                color: #333; 
                background-color: #f7f7f7; 
                line-height: 1.6; 
                padding: 10px; 
                border-radius: 8px; 
                border: 1px solid #ccc; 
            } 
            QLabel:hover { 
                background-color: #e5e5e5; 
            }
        """)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        scrollArea = QScrollArea()
        scrollArea.setWidget(label)
        scrollArea.setWidgetResizable(True)
        grid.addWidget(scrollArea)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = helpWindow()
    w.show()
    app.exec()