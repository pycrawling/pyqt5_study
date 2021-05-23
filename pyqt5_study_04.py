from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('My App')
        self.setGeometry(100, 100, 300, 300)

        self.label = QLabel('label', self)
        self.label.move(10, 10)

        self.button1 = QPushButton('button1', self)
        self.button1.move(10, 50)
        self.button1.clicked.connect(self.button_clicked)

        button2 = QPushButton('button2', self)
        button2.move(10, 100)

    def button_clicked(self):
        self.label.setText('Clicked')


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
