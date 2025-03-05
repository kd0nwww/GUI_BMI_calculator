import sys
from PyQt6.QtWidgets import QApplication
from window import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec())