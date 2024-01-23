from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys,random

class game(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Четыре буквы"
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 500
        self.icon = "4.png"
        self.currentRow = 0
        self.compWord =""
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("""
        background:'#DCDCDC';
        """)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.randomWord()
        print(self.compWord )
        grid = QGridLayout()
        grid.setRowMinimumHeight(0,30)
        grid.setRowMinimumHeight(7,30)
        grid.setColumnMinimumWidth(0,30)
        grid.setColumnMinimumWidth(6, 30)
        self.setLayout(grid)

        #МЕНЮБАР СОЗДАНИЕ
        self.menuBar = QMenuBar()
        self.filemenu = QMenu('Выбрать сложность')
        action1 = self.filemenu.addAction('4 буквы')
        action2 = self.filemenu.addAction('5 букв')
        action3 = self.filemenu.addAction('6 букв')

        self.filemenu4 = QMenu('Справка')

        self.filemenu5 = QMenu('Сложная версия')

        action1.triggered.connect(lambda: self.handle_action())
        action2.triggered.connect(lambda: self.handle_action())
        action3.triggered.connect(lambda: self.handle_action())
        self.menuBar.addMenu(self.filemenu)
        self.menuBar.addSeparator()
        self.menuBar.addMenu(self.filemenu4)
        self.menuBar.addSeparator()
        self.menuBar.addMenu(self.filemenu5)
        grid.setMenuBar(self.menuBar)


        self.titleLabel = QLabel(self.title)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setStyleSheet("""
        color:'#5C5C5C';
        font-size:46px;
        font-weight:bold;
        font-family:'Franklin Gothic Demi';
        margin:30px 30px 30px 30px;
        """)
        grid.addWidget(self.titleLabel, 0, 0, 1, 7)


        #ЗАПОЛНЕНИЕ МАССИВА
        self.ArrayBox = []
        for _ in range(6):
            self.ArrayBox.append([])
        print(self.ArrayBox)
        positions = []
        for i in range(6):
            for j in range(4):
                positions.append((i+1,j+1))
        print(positions)

        for i, position in enumerate(positions):
            self.ArrayBox[position[0] - 1].append(QLineEdit())
            grid.addWidget(self.ArrayBox[position[0] - 1][position[1] - 1], *position)


            #ВЫВОД КОРТЕЖА В ВИДЕ КУБОВ 50x50
        for i,row in enumerate(self.ArrayBox):
            for usersBox in row:
                usersBox.setMaxLength(1)
                usersBox.textEdited.connect(lambda:self.change())
                usersBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
                usersBox.setMinimumHeight(self.left*2)
                usersBox.setMinimumWidth(self.top*2)
                usersBox.setStyleSheet("""
                border:2px solid '#fffff';
                font-size:65px;
                background:'white';
                """)
                #УСЛОВИЕ НЕВОЗМОЖНОСТИ ВВОДА 5-ЗНАЧНОГО СЛОВА
                if i != self.currentRow:
                    usersBox.setReadOnly(True)
                    usersBox.setStyleSheet("""
                    border:2px solid '#fffff';
                    font-size:30px;
                    background:'light grey';
                    """)



                #1 КНОПКА (НАКРЫТЫХ ДРУГ НА ДРУГА) ОБНУЛЕНИЯ/ОБНОВЛЕНИЯ СЛОВ И РЕЗУЛЬТАТОВ
        self.messageFromUser=QLabel("")
        self.messageFromUser.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.messageFromUser.setStyleSheet("""
        font-size:26px;
        """)
        grid.addWidget(self.messageFromUser, 7, 0, 1, 7)

        self.resetButton = QPushButton("НАЧАТЬ ЗАНОВО")
        self.resetButton.setStyleSheet("""
        *{
        border:2px solid '#fffff';
        font-weight:bold;
        font-size:18px;
        font-family:'Franklin Gothic Demi';
        margin:0px 0px 30px 0px;
        color: '#0A0A0A';
        background:'#E54A98';
        }
        *:hover{
        background:'#EF0097';
        color:'white';
        }
        """)

        self.resetButton.clicked.connect(lambda:self.buttonResetClicked())
        grid.addWidget(self.resetButton,8,2,2,2)
        self.resetButton.hide()


        # 2 КНОПКА (НАКРЫТЫХ ДРУГ НА ДРУГА) ОБНУЛЕНИЯ/ОБНОВЛЕНИЯ СЛОВ И РЕЗУЛЬТАТОВ
        self.guessButton = QPushButton("ПРОВЕРИТЬ")
        self.guessButton.setStyleSheet("""
        *{
        border:2px solid '#000000';
        font-weight:bold;
        font-size:18px;
        font-family:'Franklin Gothic Demi';
        margin:0px 0px 30px 0px;
        color: '#0A0A0A';
        background:'#3BB08F';
        }
        *:hover{
        background:'#2E8B57';
        color:'white';
        }
        """)
        self.guessButton.clicked.connect(lambda:self.buttonGuessClicked())
        grid.addWidget(self.guessButton,8,2,2,2)


    #ФУНКЦИЯ ВЫВОДА СЛУЧАЙНОГО СЛОВА ИЗ ТЕКСТОВОГО ДОКУМЕНТА(СЛОВАРЯ)
    def randomWord(self):
        wordsFile = open('words4.txt', 'r', encoding="utf-8")
        words = wordsFile.read().split()
        self.compWord = random.choice(words)



    #ФУНКЦИИ КНОПКИ ПЕРЕЗАПУСКА
    def buttonResetClicked(self):
        self.randomWord()
        self.currentRow=0
        self.messageFromUser.setText("")
        for i,row in enumerate(self.ArrayBox):
            for userBox in row:
                userBox.setStyleSheet("""
                border:2px solid '#000000';
                font-size:65px;
                background:'white';
                """)
                userBox.setReadOnly(False)
                userBox.setText("")
                if i != self.currentRow:
                    userBox.setReadOnly(True)
                    userBox.setStyleSheet("""
                    border:2px solid '#000000';
                    font-size:65px;
                    background:'light grey';
                    """)
        self.buttonSwap()

    #ФУНКЦИЯ КОНПКИ ПРОВЕРКИ СЛОВА
    def buttonGuessClicked(self):
        if self.checkValid()==False:
            self.messageFromUser.setText("К сожалению данного слова нет в словаре :(")
            self.resetAll()
            self.messageFromUser.repaint()
        elif self.checkWin()==False:
            self.messageFromUser.setText(" ")
            self.messageFromUser.repaint()
            if self.currentRow < 5:
                self.colorActiveRow()
                self.activateNextRow()
            else:
                self.colorActiveRow()
                self.gameover()
        else:
            self.buttonSwap()


    #ФУНКЦИЯ ВЫДЕЛЕНИЯ БУКВ НУЖНЫМ ЦВЕТОМ
    def colorActiveRow(self):
        for i in range(4):
            self.ArrayBox[self.currentRow][i].setReadOnly(True)
            valuebox = self.ArrayBox[self.currentRow][i].text()
            if valuebox.lower() ==self.compWord[i].lower():
                self.ArrayBox[self.currentRow][i].setStyleSheet("""
                border: 2px solid '#000000';
                font-size: 65px;
                background:'#BB88FE';
                """)
            elif valuebox.lower() in self.compWord.lower():
                self.ArrayBox[self.currentRow][i].setStyleSheet("""
                border: 2px solid '#000000';
                font-size: 65px;
                background:'#37B3F3';
                """)
            else:
                self.ArrayBox[self.currentRow][i].setStyleSheet("""
                border: 2px solid '#000000';
                font-size: 65px;
                background:'grey';
                """)

    #ФУНКЦИЯ ОТКРЫВАНИЯ СЛЕДУЮЩЕГО СТОЛБЦА
    def activateNextRow(self):
        for i in range(4):
            self.ArrayBox[self.currentRow+1][i].setStyleSheet("""
                border:2px solid '#fffff';
                font-size:65px;
                background:'white';
            """)
            self.ArrayBox[self.currentRow+1][i].setReadOnly(False)
        self.currentRow=self.currentRow+1

    #ФУНКЦИЯ ПРОВЕРКИ ВВЕДЕННОГО СЛОВА ПОЛЬЗОВАТЕЛЕМ
    def checkWin(self):
        invalid = False
        count=""
        for i in self.ArrayBox[self.currentRow]:
            count=count+i.text()
        if count.lower()==self.compWord.lower():
            invalid=True
            for i in self.ArrayBox[self.currentRow]:
                i.setStyleSheet("""
                border: 2px solid '#000000';
                font-size: 65px;
                background:'#BB88FE';
                """)
                i.setReadOnly(True)
                self.messageFromUser.setText("Поздравляем! Вы выиграли!")
                self.messageFromUser.repaint()
                self.buttonSwap()
        return invalid

    #ФУНКЦИЯ ПОЯВЛЕНИЯ КНОПОК
    def buttonSwap(self):
        if self.guessButton.isVisible():
            self.resetButton.show()
            self.guessButton.hide()
        else:
            self.resetButton.hide()
            self.guessButton.show()

    #ФУНКЦИЯ ПРОВЕРКИ ПРАВИЛЬНОСТИ ВВОДА
    def checkValid(self):
        valid = True
        words = list()
        with open('words4.txt', 'r', encoding="utf-8") as f:
            words = list(str(f.read()).split())
        count = ""
        for i in self.ArrayBox[self.currentRow]:
            if not i.text().isalpha():
                valid = False
        for i in self.ArrayBox[self.currentRow]:
            count = count + i.text()
        if count.lower() not in words:
            valid=False
        return valid

    def resetAll(self):
        for i in range(4):
            self.ArrayBox[self.currentRow][i].setText('')

    def handle_action(self):
        print("dqwedw")



    #ФУНКЦИЯ ПО ОКОНЧАНИИ ПОПЫТОК
    def gameover(self):
        self.messageFromUser.setText(f"Вы проиграли,нужное слово: {self.compWord}")
        self.messageFromUser.repaint()
        self.buttonSwap()

    #ФУНКЦИЯ ПЕРЕХОДА НА СЛЕД КУБ
    def change(self):
        for i in range(3):
            if len(self.ArrayBox[self.currentRow][i].text())==1:
                self.ArrayBox[self.currentRow][i+1].setFocus()


if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = game()
    ex.show()
    sys.exit(app.exec())

#ДОБАВИТЬ В КОНТЕКСТНОЕ МЕНЮ СПРАВКУ И ПРАВИЛА ИГРЫ
#ДОБАВИТЬ ТЕМЫ,УРОВНИ,ТАЙМЕР