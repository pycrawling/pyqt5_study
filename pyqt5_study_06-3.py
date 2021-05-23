from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        groupbox = QGroupBox('성별')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        self.button0 = QRadioButton('남')
        self.button0.clicked.connect(self.button_clicked)
        self.button1 = QRadioButton('녀')
        self.button1.clicked.connect(self.button_clicked)
        self.button2 = QRadioButton('둘 다 아님')
        self.button2.clicked.connect(self.button_clicked)
        self.button3 = QRadioButton('밝힐 수 없다')
        self.button3.clicked.connect(self.button_clicked)
        self.button3.setChecked(True)

        self.line_edit = QLineEdit('')

        box_layout = QVBoxLayout()
        box_layout.addWidget(self.button0)
        box_layout.addWidget(self.button1)
        box_layout.addWidget(self.button2)
        box_layout.addWidget(self.button3)

        groupbox.setLayout(box_layout)

        layout = QVBoxLayout()
        layout.addWidget(groupbox)
        layout.addWidget(self.line_edit)

        self.setLayout(layout)

    def button_clicked(self):
        if self.button0.isChecked():
            self.line_edit.setText(self.button0.text())
        elif self.button1.isChecked():
            self.line_edit.setText(self.button1.text())
        elif self.button2.isChecked():
            self.line_edit.setText(self.button2.text())
        elif self.button3.isChecked():
            self.line_edit.setText(self.button3.text())


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
