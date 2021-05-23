from PyQt5.QtWidgets import *


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel('label')
        self.text_edit = QTextEdit('Text Edit')
        self.text_edit.setPlaceholderText('ID')
        self.button = QPushButton('Enter')
        self.button.clicked.connect(self.button_clicked)
        grid = QVBoxLayout()
        grid.addWidget(self.label)
        grid.addWidget(self.text_edit)
        grid.addWidget(self.button)
        self.setLayout(grid)

    def button_clicked(self):
        self.label.setText(self.text_edit.toPlainText())


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()