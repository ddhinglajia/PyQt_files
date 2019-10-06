#!/usr/bin/python3

# an application icon in the titlebar

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Window Icon')
        self.setWindowIcon(QIcon('web.png'))
        
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())