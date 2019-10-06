#!/usr/bin/python3

# creating statusbar

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Example(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()
    
    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())