#!/usr/bin/python3

# prints current date , date and time 

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

# returns current date
now = QDate.currentDate()

# different formats for dates
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

# returns current date and time
datetime = QDateTime.currentDateTime()

print(datetime.toString())

time = QTime.currentTime()

# returns local date and time
print(time.toString(Qt.DefaultLocaleLongDate))