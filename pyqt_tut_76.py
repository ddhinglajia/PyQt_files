#!/usr/bin/python3

# toggle button to control for background colour

import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
    QFrame)
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redbtn = QPushButton('Red', self)
        redbtn.setCheckable(True)
        redbtn.move(10, 10)

        redbtn.clicked[bool].connect(self.setColor)

        greenbtn = QPushButton('Green', self)
        greenbtn.setCheckable(True)
        greenbtn.move(10, 60)

        greenbtn.clicked[bool].connect(self.setColor)

        bluebtn = QPushButton('Blue', self)
        bluebtn.setCheckable(True)
        bluebtn.move(10, 110)

        bluebtn.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget { background-color: %s }' %
            self.col.name())
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Toggle Background Colour')
        self.show()

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0
        
        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        

        self.square.setStyleSheet('QFrame { background-color: %s }' %
            self.col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())