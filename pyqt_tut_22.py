#!/usr/bin/python3

# we select a file with a QtGui.QFileDialog and display its contents
# in a QtGui.QTextEdit

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):

        super(Example, self).__init__()

        self.initUI()
    
    def initUI(self):

        # textEdit for the file data
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar

        # for opening file, statusbar and menubar
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl++O')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(openFile)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('File open Dialog')
        self.show()
    
    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home')
        f = open(fname, 'r')

        with f:

            data = f.read()
            self.textEdit(data)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()