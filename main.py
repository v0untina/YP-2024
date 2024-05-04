import sys

from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel,  QStatusBar
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from help import helpWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(50, 50, 620, 950)
        self.setWindowTitle("Игра Пять Букв")
        self.w = None
        self.title4 = "Четыре буквы"
        self.title5 = "Пять букв"
        self.title6 = "Шесть букв"
        self.left = 50
        self.top = 50
        self.width = 620
        self.height = 950
        self.icon4 = "4.png"
        self.icon5 = "5.png"
        self.icon6 = "6.png"
        self.currentRow = 0
        self.compWord =""

        self.setStyleSheet("""
                background-color:'#DCDCDC';
                """)
        menu_bar = self.menuBar()

        levels_menu = menu_bar.addMenu("Сложность")
        levels_menu4 = levels_menu.addAction(QIcon('4.png'), "Четыре буквы")
        levels_menu4.triggered.connect(self.onMyToolBarButtonClick4)

        levels_menu5 = levels_menu.addAction(QIcon('5.png'), "Пять букв")
        levels_menu5.triggered.connect(self.onMyToolBarButtonClick5)

        levels_menu6 = levels_menu.addAction(QIcon('6.png'), "Шесть букв")
        levels_menu6.triggered.connect(self.onMyToolBarButtonClick6)

        help_menu = menu_bar.addAction("Справка")
        help_menu.triggered.connect(self.onMyToolBarButtonClickHelp)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick4(self, s):
        import words4
        self.setCentralWidget(words4.game())

    def onMyToolBarButtonClick5(self, s):
        import words5
        self.setCentralWidget(words5.game5())

    def onMyToolBarButtonClick6(self, s):
        import words6
        self.setCentralWidget(words6.game6())

    def onMyToolBarButtonClickHelp(self):
        if self.w is None:
            self.w = helpWindow()
        self.w.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()