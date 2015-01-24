###
# as we move into chapter 3 of our adventures, we appear to learning how to make
# lists. are these the same as arrays?
###

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def how_many_days(daysN):
    daysN = days_in_month[daysN - 1]
    return daysN
print how_many_days(11)

