#!/usr/bin/python3

# ToggleButton
# we create three toggle buttons.
# They will control the background color of a 
# QtGui.QFrame. 

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):

        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.col = QtGui.QColor(0, 0, 0)

        # toggle button for red, green , blue

        redb = QtGui.QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked.connect(self.setColor)

        greenb = QtGui.QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked.connect(self.setColor)

        blueb = QtGui.QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked.connect(self.setColor)

        blueb.clicked[bool].connect(self.setColor)

        # square frame for the color output
        self.square = QtGui.QFrame(self)
        self.square.setGeometry (150, 20, 100, 100)
        self.square.setStyleSheet('QWidget { background-color: %s}' %
            self.col.name())
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle Button')
        self.show()

    def setColor(self, pressed):

        #  clicked signal that operates with a Boolean value. 
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0
        
        # sets the value of the color
        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        
        self.square.setStyleSheet('QFrame { background-color: %s}' % 
            self.col.name())
        
def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()