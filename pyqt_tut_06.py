#!/usr/bin/python3

# centering window on the screen

import sys
from PyQt4 import QtGui

# QtGui.QDesktopWidget class provides information about the user's desktop
class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.resize(250,150)
        # will center the window
        self.center()

        self.setWindowTitle('Center')
        self.show()
    
    def center(self):

        # specifies rectangle geometry for the window
        qr = self.frameGeometry()
        # figures the current monitor screen resolution & the centre
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        # print(QtGui.QDesktopWidget().availableGeometry())
        # set the centre coordinates of window to centre coord. of the screen
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()