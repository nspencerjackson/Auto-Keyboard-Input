from datetime import date

def checkDate(inDay, inMonth, inYear):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    outDay = ""
    tempDay = date(inYear, inMonth, inDay).weekday()
    if tempDay != 5:
        if tempDay != 6:
            outDay = str(inDay) + "/" + str(inMonth) + "/" + str(inYear) + " (" + days[tempDay] + ")"
    return outDay

def
