#!/usr/bin/python3

# creating submenu

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu


class Example(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()
    
    def initUI(self):

        # adding a menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # adding an submenu
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())