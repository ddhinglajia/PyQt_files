#!/usr/bin/python3

# showing a tooltip


import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):

        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        # set font and font size for tooltip
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        # tooltip for two PyQt4 widgets
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        # creation a button on app
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        # location x, y for button
        btn.move(50, 50)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()