#!/usr/bin/python3

# creating an application icon

import sys
import os
from PyQt4 import QtGui

# new class that inherits from QtGui.QWidget
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    # creating GUI
    def initUI(self):
        
        # all three methods inherited from QtGui.QWidget
        # location and size of window (x, y, width, height)
        self.setGeometry(300, 300, 250, 150)
        # title of window
        self.setWindowTitle('Icon')
        # set icon for the window
        self.setWindowIcon(QtGui.QIcon('web.png'))  
        self.show()


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    