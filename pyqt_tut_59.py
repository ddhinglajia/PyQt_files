#!/usr/bin/python3

# creating a context menu
# a popup menu that appears on right click on the window

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, qApp


class Example(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context Menu')
        self.show()

    # reimplementing the contextMenuEvent() method
    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction('New')
        opnAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')
        # to get the coordinates of mouse click 
        # and thus display contextmenu accordingly
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        # defining the action outcome from the context menu
        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())