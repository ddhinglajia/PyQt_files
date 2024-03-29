#!/usr/bin/python3

# recieve data from QInputDialog dialog

import sys
from PyQt5.QtWidgets import(QWidget, QApplication, QPushButton, QLineEdit,
    QInputDialog)

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300,300, 300, 200)
        self.setWindowTitle('Input Dialog')
        self.show()

    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your Name')

        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())