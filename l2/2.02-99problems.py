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
<<<<<<< HEAD
print nextDay(2011, 12, 1)

###
# a more eloquent way to do above, not sure which is going to prove more useful.
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
=======
print nextDay(2011, 12, 1)


# a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Test procedure, will NOT produce correct ouptuts yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    years = year2 - year1
    months = month2 - month1
    days = day2 - day1
    result = years * 360 + months * 30 + days
    print result
    return result

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()