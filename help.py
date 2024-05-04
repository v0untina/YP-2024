from PyQt6.QtWidgets import QApplication,QGridLayout , QLabel, QWidget
from PyQt6.QtCore import Qt,QSize
import sys


class helpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 300, 600, 600)
        grid = QGridLayout()
        self.setFixedSize(500, 500)
        self.setLayout(grid)
        words=list()
        with open('help.txt', 'r', encoding="utf-8") as f:
            words = list(str(f.read()))
        self.setWindowTitle("Справка")
        label=QLabel(''.join(map(str,words)))
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        label.setStyleSheet("""
        font-size:16px;
        """)
        grid.addWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = helpWindow()
    w.show()
    app.exec()