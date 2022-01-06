from KeybMouse import *
from Calend import *
from datetime import date

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
beforeFriday = True

fridayTime = 1
mondayTime = 1

# Gets the integer value of what month is next
nextMonth = nxtMonth(date.today().month)

# Checks if the next month is in a new year or not
if nextMonth == 1:
    year = date.today().year + 1
else:
    year = date.today().year

# x and y coordinates of Temp Tab
xTemplate = 786
yTemplate = 85
# x and y coordinates of Friday Page
xFriday = 1801
yFriday = 178
# x and y coordinates of Weekday Page
xWeekday = 1799
yWeekday = 155
# x and y coordinates of the bottom right Friday Tables
xBottomFriday = 927
yBottomFriday = 745
# x and y coordinates of bottom right Weekday Tables
xBottomWeekday = 930
yBottomWeekday = 575
# x and y coodinates of the top of both tables
xTopTable = 45
yTopTable = 236
# x and y coordinates of new month tab
xMonth = 357
yMonth = 90
# x and y coordinates of Add Page button
xAddPage = 1776
yAddPage = 117

# sleeps program for 1 second so it doesn't run on wrong window
time.sleep(1)

# Changes window
alt_tab()
time.sleep(0.05)

# Open Weekday Table first to have in Clipboard
moveMouse(xTemplate, yTemplate)
clickMouse()
moveMouse(xWeekday, yWeekday)
clickMouse()

# Copy Weekday Table
copy(xBottomWeekday, yBottomWeekday, xTopTable, yTopTable, mondayTime)
moveMouse(xMonth, yMonth)
clickMouse()

# Adds a new Page to month tab
moveMouse(xAddPage, yAddPage)
clickMouse()

# Cycles through month (day-by-day)
for i in range(months[nextMonth-1]):
    # Checks if it is a weekday
    if weekendCheck(i+1, date.today().month, year):
        # Gets the date in the format "dd/mm/yy (Day)"
        d = checkDate(i+1, date.today().month, year)
        # Checks if it is a Friday
        if (beforeFriday) and (fridayCheck(i+1, nextMonth, year)):
            # Opens Template tab
            moveMouse(xTemplate, yTemplate)
            clickMouse()
            # Opens Friday Page
            moveMouse(xFriday, yFriday)
            clickMouse()
            # Copies Friday table
            copy(xBottomFriday, yBottomFriday, xTopTable, yTopTable, fridayTime)
            # No longer first time copying table
            if fridayTime == 1:
                fridayTime = 2
            # It is Friday, allows to enter other side of if-statement
            beforeFriday = False
            # Goes to Month tab
            back_to_month(xMonth, yMonth)
        # If not friday, but it is Monday
        elif (not beforeFriday) and (not fridayCheck(i+1, nextMonth, year)):
            # Opens template tab
            moveMouse(xTemplate, yTemplate)
            clickMouse()
            # Opens Weekday Page
            moveMouse(xWeekday, yWeekday)
            clickMouse()
            # Copies Weekday Table
            copy(xBottomWeekday, yBottomWeekday, xTopTable, yTopTable, mondayTime)
            # No longer first time copying table
            if mondayTime == 1:
                mondayTime = 2
            # Still before Friday
            beforeFriday = True
            # Goes back to Month tab
            back_to_month(xMonth, yMonth)
        # prints out the date
        type_key(d)
        # Pastes Table into OneNote page
        tab()
        paste()
        if i != 30:
            moveMouse(xAddPage, yAddPage)
            clickMouse()
# Right click on first page in tab
moveMouse(1792, 155)
clickMouseRight()
# Deletes page
moveMouse(1670, 201)
clickMouse()
