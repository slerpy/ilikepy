###
# code to check for days between 2 dates.
# accounts for leap years, days in each month, etc..
###


def nextDay(year, month, day):
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day < 30:
            return year, month, day + 1
        else:
            if month < 12:
                return year, month + 1, 1
            else:
                return year + 1, 1, 1
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day < 31:
                return year, month, day + 1
            else:
                if month < 12:
                    return year, month + 1, 1
                else:
                    return year + 1, 1, 1
    else:
        if month == 2:
            if year % 4 == 0 and year % 100 != 0:
                if day < 29:
                   return year, month, day +1
                else:
                    if month < 12:
                        return year, month + 1, 1
                    else:
                        return year + 1, 1, 1
            elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
                if day < 29:
                    return year, month, day + 1
                else:
                    if month < 12:
                       return year, month + 1, 1
                    else:
                        return year + 1, 1, 1
            else:
                if day < 28:
                        return year, month, day + 1
                else:
                    if month < 12:
                        return year, month + 1, 1
                    else:
                        return year + 1, 1, 1
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    daysN = 0
    while year1 != year2 or month1 != month2 or day1 != day2:
        year1, month1, day1 = nextDay(year1, month1, day1)
        daysN = daysN + 1
    return daysN

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()