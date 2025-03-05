from PyQt6.QtWidgets import QMainWindow, QGraphicsBlurEffect, QApplication, QDialog, QLabel, QPushButton, QVBoxLayout
from design import Ui_MainWindow

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 796, 593)
        self.setWindowTitle("BMI Calculator")

        self.ui.calculate_button.clicked.connect(self.calculate_bmi)
        self.ui.measurement_system.currentIndexChanged.connect(self.change_units)
        self.ui.actionClear.triggered.connect(self.clear)
        self.ui.actionExit.triggered.connect(QApplication.quit)

    def calculate_bmi(self):
        blur_effect1 = QGraphicsBlurEffect()
        blur_effect1.setBlurRadius(5)
        blur_effect2 = QGraphicsBlurEffect()
        blur_effect2.setBlurRadius(5)
        blur_effect3 = QGraphicsBlurEffect()
        blur_effect3.setBlurRadius(5)

        weight = int(self.ui.weight_input.text())
        height = int(self.ui.height_input.text())

        if self.ui.measurement_system.currentText() == "Imperial":
            bmi = round((weight / (height ** 2)) * 703, 1)
        
        elif self.ui.measurement_system.currentText() == "Metric":
            bmi = round(weight / (height / 100) ** 2, 1)

        self.ui.bmi_label.setText(f'Your BMI is {str(bmi)}')

        if bmi < 18.5:
            self.ui.underweight_label.move(70, 420)
            self.ui.normal_weight_label.setGraphicsEffect(blur_effect1)
            self.ui.overweight_label.setGraphicsEffect(blur_effect2)
            self.ui.obese_label.setGraphicsEffect(blur_effect3)

        elif 18.5 <= bmi <= 24.9:
            self.ui.normal_weight_label.move(240, 420)
            self.ui.underweight_label.setGraphicsEffect(blur_effect1)
            self.ui.overweight_label.setGraphicsEffect(blur_effect2)
            self.ui.obese_label.setGraphicsEffect(blur_effect3)

        elif 25 <= bmi <= 30:
            self.ui.overweight_label.move(410, 420)
            self.ui.obese_label.setGraphicsEffect(blur_effect1)
            self.ui.underweight_label.setGraphicsEffect(blur_effect2)
            self.ui.normal_weight_label.setGraphicsEffect(blur_effect3)

        elif bmi > 30:
            self.ui.obese_label.move(580, 420)
            self.ui.underweight_label.setGraphicsEffect(blur_effect1)
            self.ui.normal_weight_label.setGraphicsEffect(blur_effect2)
            self.ui.overweight_label.setGraphicsEffect(blur_effect3)

    def change_units(self):

        if self.ui.measurement_system.currentText() == "Imperial":
            self.ui.units_weight.setText("lbs")
            self.ui.units_height.setText("in")
        
        elif self.ui.measurement_system.currentText() == "Metric":
            self.ui.units_weight.setText("kg")
            self.ui.units_height.setText("cm")

    def clear(self):
        self.ui.weight_input.clear()
        self.ui.height_input.clear()
        self.ui.bmi_label.clear()
        self.ui.underweight_label.move(70, 460)
        self.ui.normal_weight_label.move(240, 460)
        self.ui.overweight_label.move(410, 460)
        self.ui.obese_label.move(580, 460)
        self.ui.underweight_label.setGraphicsEffect(None)
        self.ui.normal_weight_label.setGraphicsEffect(None)
        self.ui.overweight_label.setGraphicsEffect(None)
        self.ui.obese_label.setGraphicsEffect(None)