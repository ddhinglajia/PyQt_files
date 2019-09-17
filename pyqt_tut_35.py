#!/usr/bin/python3

# drawing points

import sys
import random
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):

        super(Example, self).__init__()

        self.initUI()
    
    def initUI(self):

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Random Paints')
        self.show()
    
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end(self)

    def drawPoints(self, qp):

        qp.setPen(QtCore.Qt.blue)
        size = self.size()

        for i in range(5000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)
        
def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()