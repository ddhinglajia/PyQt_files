#!/usr/bin/python3

# closing a window with a button

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip)

class Example(QWidget):

    def  __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.setToolTip('To exit the window')
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Quit Button')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())