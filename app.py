from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.styles.setGraphicsEffect(self.shadow)
        self.changeTheme()
        self.theme_btn.clicked.connect(self.changeTheme)
        self.navMove.mouseMoveEvent = self.moveWindow
        self.minimizeAppBtn.clicked.connect(self.showMinimized)
        self.maximizeRestoreAppBtn.clicked.connect(self.showMaximized)
        self.closeAppBtn.clicked.connect(self.close)
        
        
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


    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
    def moveWindow(self,event):
        # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
            
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())