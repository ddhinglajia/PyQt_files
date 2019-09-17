#!/usr/bin/python3

# QtGui.QSplitter

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):

        super(Example, self).__init__()

        self.initUI()
    
    # 3 widget frames and 2 splitter (vertical and horizontal)
    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)

        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)

        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        # creating horizontal splitter
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        # boundries for splitter
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        # creating vertical splitter
        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        # boundaries for splitter
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        # cleanlooks is a predefined style
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QtGui.QSplitter')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()