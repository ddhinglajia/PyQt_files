#!/usr/bin/python3

# QtGui.QCheckBox
# check boxes for enable or disable

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):

        super(Example, self).__init__()

        self.initUI()
    
    def initUI(self):

            # creating a checkbox
        cb = QtGui.QCheckBox('Show Title', self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('QtGui.QCheckBox')
        self.show()

    def changeTitle(self, state):

        # toggle to show/stop showing the window title
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()