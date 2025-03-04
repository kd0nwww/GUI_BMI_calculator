from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("BMI Calculator")