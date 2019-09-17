#!/usr/bin/python3

# QtGuiQPixmap

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):

        super(Example, self).__init__()

        self.initUI()
    
    def initUI(self):

        # display an image on the window
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap('web.png')

        lbl = QtGui.QLabel(self)
        # creates a QtGui.QPixmap object
        # It takes the name of the file as a parameter. 
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('web')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()