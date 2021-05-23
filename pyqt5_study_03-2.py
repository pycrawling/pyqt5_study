from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):  # QMainWindow 를 상속합니다.
    def __init__(self):
        super().__init__()  # 부모 클래스의 초기화 메서드를 가져와 실행합니다.
        self.setWindowTitle('My App')
        self.setGeometry(100, 100, 300, 300)


app = QApplication([])
my_window = MyWindow()
my_window.show()
app.exec_()
