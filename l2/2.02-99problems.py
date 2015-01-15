###
# a procedure to add one day to a calendar, assuming all months are 30 days.
# a test run into building a full calendar.
###

def nextDay(year, month, day):
    if day == 30:
        day = 1
        if month == 12:
            month = 1
            year = year + 1
        else:
            month = month + 1
    else:
        day = day + 1

    return(year, month, day)
print nextDay(2011, 12, 1)