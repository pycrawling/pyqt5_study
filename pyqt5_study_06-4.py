from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        groupbox = QGroupBox('가지고 싶은 필기구')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        self.button0 = QCheckBox('연필')
        self.button0.stateChanged.connect(self.button_changed)
        self.button1 = QCheckBox('지우개')
        self.button1.stateChanged.connect(self.button_changed)
        self.button2 = QCheckBox('볼펜')
        self.button2.stateChanged.connect(self.button_changed)
        self.button3 = QCheckBox('샤프')
        self.button3.stateChanged.connect(self.button_changed)

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

    def button_changed(self):
        message = []
        if self.button0.isChecked():
            message.append(self.button0.text())
        if self.button1.isChecked():
            message.append(self.button1.text())
        if self.button2.isChecked():
            message.append(self.button2.text())
        if self.button3.isChecked():
            message.append(self.button3.text())
        self.line_edit.setText(', '.join(message))


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
