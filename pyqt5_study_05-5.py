from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit('0')
        self.button0 = QPushButton('0')
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        self.button9 = QPushButton('9')
        self.button_add = QPushButton('+')
        self.button_sub = QPushButton('-')
        self.button_mul = QPushButton('*')
        self.button_div = QPushButton('/')
        self.button_clear = QPushButton('C')
        self.button_dot = QPushButton('.')
        self.button_equal = QPushButton('=')

        layout_upper = QHBoxLayout()
        layout_upper.addWidget(self.line_edit)
        layout_upper.addWidget(self.button_clear)

        layout_lower = QGridLayout()
        layout_lower.addWidget(self.button7, 0, 0)
        layout_lower.addWidget(self.button8, 0, 1)
        layout_lower.addWidget(self.button9, 0, 2)
        layout_lower.addWidget(self.button4, 1, 0)
        layout_lower.addWidget(self.button5, 1, 1)
        layout_lower.addWidget(self.button6, 1, 2)
        layout_lower.addWidget(self.button1, 2, 0)
        layout_lower.addWidget(self.button2, 2, 1)
        layout_lower.addWidget(self.button3, 2, 2)
        layout_lower.addWidget(self.button0, 3, 0)
        layout_lower.addWidget(self.button_dot, 3, 1)
        layout_lower.addWidget(self.button_equal, 3, 2)
        layout_lower.addWidget(self.button_sub, 0, 3)
        layout_lower.addWidget(self.button_div, 1, 3)
        layout_lower.addWidget(self.button_mul, 2, 3)
        layout_lower.addWidget(self.button_add, 3, 3)

        layout = QVBoxLayout()
        layout.addLayout(layout_upper)
        layout.addLayout(layout_lower)
        self.setLayout(layout)


app = QApplication([])
my_window = MyWidget()
my_window.show()
app.exec_()
