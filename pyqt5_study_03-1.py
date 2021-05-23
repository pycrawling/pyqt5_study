from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication([])
my_window = QMainWindow()
my_window.setWindowTitle('My App')
my_window.setGeometry(100, 100, 300, 300)
my_window.show()
app.exec_()
