#!/usr/bin/python3

# difference betweern dates in days
# added user input of two dates

from PyQt5.QtCore import QDate

# xmas1 = QDate(2018, 12, 24)
# xmas2 = QDate(2019, 12, 24)

# now = QDate.currentDate()

# dayspassed = xmas1.daysTo(now)

# print("{0} days have passes from since the last Christmas".format(dayspassed))

# daysremaining = now.daysTo(xmas2)

# print('{0} days remaining to christmas this year'.format(daysremaining))

userdate = input(
    'Enter the date from which you needs the days calculated in YYYY-MM-DD : ')

y, m, d = map(int, userdate.split('-'))
dateu1 = QDate(y, m, d)


userdate = input(
    'Enter the date to which you needs the days calculated in YYYY-MM-DD : ')

y, m, d = map(int, userdate.split('-'))
dateu2 = QDate(y, m, d)

print('{0} number of days to the second date'.format(dateu1.daysTo(dateu2)))