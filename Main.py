from KeybMouse import *
#from Calend import *

beforeFriday = True

fridayTime = 1
mondayTime = 1

# x and y coordinates of Temp Tab
xTemplate = 907
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
xMonth = 263
yMonth = 90
# x and y coordinates of Add Page button
xAddPage = 1776
yAddPage = 117

# sleeps program for 1 second so it doesn't run on wrong window
time.sleep(1)

# Changes window
#alt_tab()
time.sleep(0.05)

moveMouse(xTemplate, yTemplate)
moveMouse(xFriday, yFriday)
moveMouse(xWeekday, yWeekday)
moveMouse(xBottomFriday, yBottomFriday)
moveMouse(xBottomWeekday, yBottomWeekday)
moveMouse(xTopTable, yTopTable)
moveMouse(xMonth, yMonth)
moveMouse(xAddPage, yAddPage)
