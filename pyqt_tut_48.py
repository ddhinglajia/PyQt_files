#!/usr/bin/python3

# julian day

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

print('Georgian date for today: ', now.toString(Qt.ISODate))

print('Julian day for today: ', now.toJulianDay())