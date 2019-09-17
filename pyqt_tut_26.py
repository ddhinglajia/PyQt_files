#!/usr/bin/python3

# QtGui.QProgressBar

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):

        super(Example, self).__init__()

        self.initUI()
    
    def initUI(self):

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QtGui.QPushButton('Start', self)
        self.btn.move(40, 80 )
        