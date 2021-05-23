from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.addWidget(QPushButton('AAA'))
        layout.addWidget(QPushButton('BBB'))
        layout.addWidget(QPushButton('CCC'))
        self.setLayout(layout)


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
