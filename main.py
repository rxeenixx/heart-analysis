from PyQt5.QtCore import Qt, QTime, QTimer, QLocale
from PyQt5.QtGui import QDoubleValidator,QIntValidator, QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QVBoxLayout, QGridLayout, QGroupBox, QRadioButton,
                             QPushButton, QLabel, QListWidget, QLineEdit)
from text import *
from heart import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text,alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()
main()
