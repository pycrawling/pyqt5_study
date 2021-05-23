from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])

my_window = QMainWindow()
my_window.setWindowTitle('My App')
my_window.setGeometry(100, 100, 300, 300)

# QPushButton 의 첫번째 인수는 버튼의 Title 입니다.
# 두번째 인수는 상위 위젯을 의미합니다.
# 버튼은 my_window 의 내부에 있게됩니다.
button1 = QPushButton('Click me', my_window)
button1.move(10, 10)

my_window.show()
app.exec_()
