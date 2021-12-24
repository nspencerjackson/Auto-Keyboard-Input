from datetime import date

def checkDate(inDay, inMonth, inYear):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    outDay = ""
    tempDay = date(inYear, inMonth, inDay).weekday()
    if tempDay != 5:
        if tempDay != 6:
            outDay = str(inDay) + "/" + str(inMonth) + "/" + str(inYear) + " (" + days[tempDay] + ")"
    return outDay

def weekendCheck(inDay, inMonth, inYear):
    wknd = False
    temp = date(inYear, inMonth, inDay).weekday()
    if temp != 5:
        if temp != 6:
            wknd = True
    return wknd

def fridayCheck(inDay, inMonth, inYear):
    friday = False
    temp = date(inYear, inMonth, inDay).weekday()
    if temp == 4:
        friday = True
    return friday

def nxtMonth(inMonth):
    nextMonth = inMonth + 1
    if nextMonth == 13:
        nextMonth = 1
    return nextMonth
