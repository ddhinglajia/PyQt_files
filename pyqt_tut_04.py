#!/usr/bin/python3

# closing a window
# create a button to quit when clicked it exit the application

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        # creating a pushbutton for quitting
        # button is an instance of QtGui.QPushButton
        qbtn = QtGui.QPushButton('Quit', self)
        # QtCore.QCoreApplication contains the main event loop
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()