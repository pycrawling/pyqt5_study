from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.addWidget(QPushButton('AAA'), 0, 0)
        layout.addWidget(QPushButton('BBB'), 0, 1)
        layout.addWidget(QPushButton('CCC'), 1, 1)
        self.setLayout(layout)


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
