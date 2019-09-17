#!/usr/bin/python3

# Drawing text (Russian azbuka)

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):

        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.text = '\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw Text')
        self.show()

    #  draw some text in Cylliric
    def paintEvent(self, event):

        qp = QtGui.QPainter()
        # all painiting occurs between begin and end
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()
    
    # method draws text
    def drawText(self, event, qp):

        qp.setPen(QtGui.QColor(164, 34, 31))
        # sets the font for drawing the text
        qp.setFont(QtGui.QFont('Decorative', 10))
        # sets the paint event in rectangle and centres the text
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()