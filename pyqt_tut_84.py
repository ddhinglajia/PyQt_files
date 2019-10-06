#!/usr/bin/python3

# example for simple drag and drop

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton

class Button(QPushButton):

    def __init__(self, title, parent):

        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
        
    def dropEvent(self, e):

        self.setText(e.mimeData().text())
    

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()
    
    def initUI(self):

        edit = QLineEdit(self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        btn = Button('Button', self)
        btn.move(190, 65)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Simple Drag and Drop')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())