#!/usr/bin/python3

import sys
from PyQt4 import QtGui


def main():
    
    # creating an application object
    app = QtGui.QApplication(sys.argv)

    # defualt constructor for QtGui
    # widget without parent called window
    w = QtGui.QWidget()
    # resizes the size of the widget
    w.resize(250, 150)
    # postions the widget to screen coordinates
    w.move(300, 300)
    # gives title to the ttle bar
    w.setWindowTitle('Simple')
    # displays the widget on the screen
    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()