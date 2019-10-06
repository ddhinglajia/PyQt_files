#!/usr/bin/python3

# absolute ositioning of labels

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 20)

        lbl2 = QLabel('Tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for Programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute Positioning')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())