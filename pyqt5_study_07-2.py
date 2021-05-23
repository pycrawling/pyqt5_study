from PyQt5.QtWidgets import *
from PyQt5 import uic

ui = uic.loadUiType('pyqt5_study_07-1.ui')[0]


class MyWindow(QWidget, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
