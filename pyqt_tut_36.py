#!/usr/bin/python3

# draw 3 rectangles with 3 different colours

import sys
from PyQt4 import QtCore, QtGui

class Example(QtGui.QWidget):

    def __init__(self):

        super(Example, self).__init__()

        self.initUI()
    
    def initUI(self):

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Coloured Rectangles')
        self.show()
    
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end(self)

    # to create rectangle and assign colours respectively
    def drawRectangles(self, qp):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QtGui.QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()