"""import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QLabel

def calculate_fact():
    result=1
    for i in range(1,100):
        result*=i
    return result


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Freezing Example")
        self.setGeometry(100,100,300,200)

        self.label=QLabel(self)
        self.label.setGeometry(50,50,200,30)

        self.button=QPushButton("Calculate Facturial")
        self.button.setGeometry(50,100,300,30)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        factorial=calculate_fact()
        self.label.setText(f"Factorial: { factorial}")
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

def calculate_factorial():
    result = 1
    for i in range(1, 10):
        result *= i
    return result

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Freezing Example")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 200, 30)

        self.button = QPushButton("Calculate Factorial", self)
        self.button.setGeometry(50, 100, 200, 30)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        factorial = calculate_factorial()
        self.label.setText(f"Factorial: {factorial}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
