#!/usr/bin/python3

# creating menubar for the window

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example,self).__init__()

        self.initUI()
    
    def initUI(self):
        

        # creating an action with exiit
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        # creating a shortcut for the action
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()
        
        # crating a drop down menubar with predefined action
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menubar')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
