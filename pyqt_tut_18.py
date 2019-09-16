#!/usr/bin/python3

# emitting signals

import sys
from PyQt4 import QtGui, QtCore

class Communicate(QtCore.QObject):
    # signal is emitted during a mouse press event to close the window
    closeApp = QtCore.pyqtSignal() 


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()
    
    def initUI(self):
        
        self.c = Communicate()
        # A signal is created with the QtCore.pyqtSignal() as 
        # a class attribute of the external Communicate class. 
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit Signal')
        self.show()

    def mousePressEvent(self, event):

        self.c.closeApp.emit()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()