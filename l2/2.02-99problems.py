####
# a procedure to add one day to a calendar, assuming all months are 30 days.
# a test run into building a full calendar.
####

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

###
# another way to do above
###

def nextDay2(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year +1, 1, 1
print nextDay2(2098, 11, 13)