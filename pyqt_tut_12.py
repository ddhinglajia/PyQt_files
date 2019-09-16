#!/usr/bin/python3

# box layout
# The example places two buttons in the bottom-right corner of the window

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()
    
    def initUI(self):

        # create two ok and cancel button
        okButton = QtGui.QPushButton('OK')
        cancelButton = QtGui.QPushButton('Cancel')

        # create a horizontal box layout 
        # and add a stretch factor and both buttons
        hbox = QtGui.QHBoxLayout()
        hbox.addSpacing(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # create by putting a horizontal layout into a vertical one
        vbox = QtGui.QVBoxLayout()
        # The stretch factor in the vertical box will 
        # push the horizontal box with the buttons to the bottom of the window 
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 600, 350)
        self.setWindowTitle('Buttons')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()