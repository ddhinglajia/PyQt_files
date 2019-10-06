#!/usr/bin/python3

# example of using QCalenderWidget

import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
    QVBoxLayout, QCalendarWidget)
from PyQt5.QtCore import QDate

class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()
    
    def initUI(self):

        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        
        self.setLayout(vbox)

        self.setGeometry(300, 300, 550, 500)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):

        self.lbl.setText(date.toString())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())