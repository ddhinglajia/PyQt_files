#!/usr/bin/python3

# creating a message box

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message Box')
        self.show()

    def closeEvent(self, event):

        # message box with two buttons: Yes and No
        # If we close a QtGui.QWidget, a QtGui.QCloseEvent is generated
        reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure to quit?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
