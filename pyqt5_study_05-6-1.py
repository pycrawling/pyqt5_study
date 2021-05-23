from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow,
                             QPushButton, QVBoxLayout, QWidget)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel('label')
        self.button1 = QPushButton('button1')
        self.button1.clicked.connect(self.button1_clicked)
        self.button2 = QPushButton('button2')
        self.button2.clicked.connect(self.button2_clicked)

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button1_clicked(self):
        self.label.setText('Clicked')

    def button2_clicked(self):
        self.label.setText('')


app = QApplication([])
my_window = MyWidget()
my_window.show()
app.exec_()
