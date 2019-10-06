#!/usr/bin/python3

# daylight saving time

from PyQt5.QtCore import QDateTime, QTimeZone, Qt

now = QDateTime.currentDateTime()

print('Time zone: {0}'.format(now.timeZoneAbbreviation()))

if now.isDaylightTime():
    print('The current date falls in DST time.')
else:
    print('The current date does not fall into DST time.')
