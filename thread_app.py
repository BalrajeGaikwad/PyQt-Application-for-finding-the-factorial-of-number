import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import QThread, pyqtSignal

class FactorialThread(QThread):
    result_ready = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        result = 1
        for i in range(1, 100000):
            result *= i
        self.result_ready.emit(result)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QThread Example")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 200, 30)

        self.button = QPushButton("Calculate Factorial", self)
        self.button.setGeometry(50, 100, 200, 30)
        self.button.clicked.connect(self.on_button_click)

        self.thread = FactorialThread()
        self.thread.result_ready.connect(self.on_factorial_calculated)

    def on_button_click(self):
        self.button.setEnabled(False)
        self.thread.start()

    def on_factorial_calculated(self, result):
        self.label.setText(f"Factorial: {result}")
        self.button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
