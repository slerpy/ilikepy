#
# obligatory

print "hello world!"

#
# minutes in 7 weeks

print 7 * 7 * 24 * 60

#
# how far does light travels in centimeters in one nanosecond
# speed of light = 299,272,258 meters/second
# nanosecond = 1/1,000,000,000

print 299792458 * 100 * 1/1000000000

# if i don't want python to round this down, i need to what? add decimals?
print 299792458.0 * 100 * 1.0/1000000000

# :)
# assigning variables: name = expression
#
speed_of_light = 299792458.0 # meters per second
cycles_per_second = 2700000000.0 # 2.7GHz
cycle_distance = speed_of_light/cycles_per_second
print cycle_distance

#
# doo doo doo. we're assigning new values because = does not mean equal, it means assign ...
#

hours = 9
hours = hours + 1
hours = hours * 2
print hours

#
# hammer the variables thing hooome!
# btw, i can't find out howo to add line numbers in pycharm. ( found it :)

age = 26 # spirit age
days_alive = age * 365
print days_alive

#
# i touched it and it was all stringy.
#

name = "shaden"
print name
print "hello " + name
