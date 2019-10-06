#!/usr/bin/python3

# create and postions button on the window

import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, 
    QHBoxLayout, QVBoxLayout)

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        # creating buttons
        okBtn = QPushButton('OK')
        cancelBtn = QPushButton('Cancel')

        # creating horizontal boxes layout for the buttons
        hbox = QHBoxLayout()
        # stretch factor = 1 adds stretchable space for beofre the two buttons
        hbox.addStretch(1)
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        # creating a vertical box layout for the hbox layout
        vbox = QVBoxLayout()
        # stretch factor = 1 here will push the hbox to bottom of the window
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # creates the main layout of the window
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())