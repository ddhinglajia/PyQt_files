#!/usr/bin/python3

# creating colour dilog

import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, 
    QFrame, QColorDialog)
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.iniUI()

    def iniUI(self):

        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dilog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.setStyleSheet('QWidget { background-color: %s }'
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color Dialog')
        self.show()

    def showDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }'
                % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())