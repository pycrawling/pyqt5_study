from PyQt5.QtWidgets import *


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.line_edit1 = QLineEdit('')
        self.line_edit1.setPlaceholderText('ID')
        self.line_edit1.textChanged.connect(self.line_edit_text_changed)
        self.line_edit2 = QLineEdit('')
        self.line_edit2.setPlaceholderText('PASSWORD')
        self.line_edit2.setEchoMode(QLineEdit.Password)
        self.line_edit2.returnPressed.connect(self.line_edit_return_pressed)
        self.label = QLabel('label')
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit1)
        layout.addWidget(self.line_edit2)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def line_edit_text_changed(self):
        self.label.setText(self.line_edit1.text())

    def line_edit_return_pressed(self):
        self.label.setText(self.line_edit2.text())


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
