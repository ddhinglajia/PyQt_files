#!/usr/bin/python3

# QtGui.QGridLayout
# create a grid layout with rows and columns
# create a skeleton of a calculator

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # apllication layout as a list
        names = [ 'Cls', 'Bck', '', 'Close',
                    '7', '8', '9', '/',
                    '6', '5', '4', '*',
                    '3', '2', '1', '-',
                    '0', '.', '=', '+']
        
        # creating a ist of coordinates from (0,0) to (4,3)
        positions = [(i,j) for i in range(5) for j in range(4)]

        # zip function creates a tuple object with iterators of variables 
        # in argument
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()