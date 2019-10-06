#!/usr/bin/python3

# number of days
# added date input form the user

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

userdate = input('Enter the date in YYYY-MM-DD: ')
y, m, d = map(int, userdate.split('-'))
# qdate take as yyyy, mm, dd
dateu = QDate(y, m, d)
date1 = QDate(1947, 6, 7)

# prints the days in the month for the date specified
print("Days in month: {0}".format(dateu.daysInMonth()))
# prints the day in the year for the specified date
# print("Days in year: {0}".format(d.daysInYear()))


# prints the days in the month for the current date 
print("Days in the current month: {0}".format(date1.daysInMonth()))
# prints the day in the year for the current date
# print("Days in year: {0}".format(d.daysInYear()))