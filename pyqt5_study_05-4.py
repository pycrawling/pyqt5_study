from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QFormLayout()
        layout.addRow(QPushButton('AAA'), QPushButton('BBB'))
        layout.addRow(QPushButton('CCC'), QPushButton('DDD'))
        self.setLayout(layout)


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
