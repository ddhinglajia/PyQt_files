#!usr/bin/python3

# creating a message box using PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Example(QWidget):
    
    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Message Box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                'Are you sure you want to close the window?', QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
            
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
