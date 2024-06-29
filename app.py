from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.changeTheme()
        self.theme_btn.clicked.connect(self.changeTheme)
        
    def darkMode(self):
        self.styles.setStyleSheet(open("dark-mode.qss", "r").read())
    def lightMode(self):
        self.styles.setStyleSheet(open("light-mode.qss", "r").read())
        
    def changeTheme(self):
        if self.theme_btn.isChecked():
            print("Dark Mode")
            self.theme_btn.setStyleSheet(
                "background-image: url(:/dark_blue/img/sun.png);"
                "background-repeat:no-repeat;"
                "background-position: center;"
            "")
            self.darkMode()
        else:
            print("Light Mode")
            self.theme_btn.setStyleSheet(
                "background-image: url(:/dark_blue/img/moon.png);"
                "background-repeat:no-repeat;"
                "background-position: center;"
            "")
            self.lightMode()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())