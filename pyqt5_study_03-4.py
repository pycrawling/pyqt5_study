from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('My App')
        self.setGeometry(100, 100, 300, 300)

        button1 = QPushButton('Click me', self)
        button1.move(10, 10)


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
