#!/usr/bin/python3

# example for QComboBox

import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
    QComboBox)

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl = QLabel('Ubuntu', self)
        
        combo = QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Fedora')
        combo.addItem('ArchLinux')
        combo.addItem('LinuxMint')
        combo.addItem('Mandriva')

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())