#!/usr/bin/python3

# creating a menubar, toolbar and a status bar
# skeleton of classic GUI application 
# some deviations from zetcode tutorials

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QTextEdit, QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()
    
    def initUI(self):

        # creating a writable space
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # creating statusbar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        # creating actions
        newAct = QAction('New', self)
        opnAct = QAction('Open', self)
        impMailAct = QAction('Import Mail', self)

        # creating submenu
        impMenu = QMenu('Import', self)
        impMenu.addAction(impMailAct)

        # creating exit action with shortvut and statusbar tip
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(self.close)

        #creating the menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAct)
        fileMenu.addAction(opnAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)

        # creating the toolbar with exit action
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Main Window')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())