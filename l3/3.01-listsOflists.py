###
# as we move into chapter 3 of our adventures, we appear to be learning how to make
# lists. are these the same as arrays?
###


###
# procedure to figure out how many days in any chosen month
# assumes non leap year
###

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def how_many_days(month):
    return days_in_month[month - 1]
print how_many_days(11)


###
# just testing slerping stuff out from lists
###

countries = [['China','Beijing',1350],
             ['India','New Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington DC',307]]

# india capital
print countries[1][1]
# multiple of romanias pop to china
print countries[0][2] / countries[2][2]


###
# mutate stooges to get rid of curly and replace with shemp
###


stooges = ['Moe','Larry','Curly']
stooges[2] = 'Shemp'
print stooges

