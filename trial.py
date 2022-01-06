from KeybMouse import *
import time

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

def tryMouse(x,y):
    moveMouse(x, y)
    clickMouse()
    time.sleep(0.5)

tryMouse(xTemplate, yTemplate)
tryMouse(xFriday, yFriday)
tryMouse(xWeekday, yWeekday)
tryMouse(xBottomFriday, yBottomFriday)
tryMouse(xBottomWeekday, yBottomWeekday)
tryMouse(xTopTable, yTopTable)
tryMouse(xMonth, yMonth)
tryMouse(xAddPage, yAddPage)
