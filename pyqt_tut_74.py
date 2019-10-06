#!/usr/bin/python3

# select file and display its contents

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction,
    QTextEdit, QFileDialog)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()
    

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):

        # opens file dialog from /home
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home')

        # opens the file in read only
        # cpies the the content as data
        # and send the data as string to the created dialog
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())