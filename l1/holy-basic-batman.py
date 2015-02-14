#
# obligatory
#
print "hello world!"

#
# minutes in 7 weeks
#
print 7 * 7 * 24 * 60

#
# how far does light travels in centimeters in one nanosecond
# speed of light = 299,272,258 meters/second
# nanosecond = 1/1,000,000,000
#
print 299792458 * 100 * 1/1000000000

#
# if i don't want python to round this down, i need to what? add decimals?
#
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
#
age = 26 # spirit age
days_alive = age * 365
print days_alive

#
# i touched it and it was all stringy.
#
name = "shaden "
print name
print "hello " + name

#
# echo echo echo
#
print "hello " + name * 3

#
# Indexing strings, brackets [] extract from strings. strings start with 0
#
print name[0] # should return s
print name [1+2] # should return 4th letter (d), 0(s) 1(h) 2(a) 3(d) 4(e) 5(n) 6( )

#
# - symbols start at end of string. ex, name [-2] should return n (because var name has a space at the end.)
#
print name [-2]

#
# we can concatenate vars together if they are strings. shaden shaden
#
print name + name

#
# sub sequences x:y x=start y=stop. sucks out left of x --> y-1 so name [0:5] should return shade.
# think cursor position left of first letter would be 0(s) count over to after e(5)
# if we leave the right side of colon empty, it will take from first selection to the end. ex, name [3:] should pull out den
# if we leave the left side of the colon empty, it will take from beginning of string to end spot. ex, name [:5] will return shade
#
print name [0:5]
print name [3:]
print name [:5]


#
#
#
s = "iamshaden"
print s[3:].capitalize()

s = s [3:]
print s.capitalize()

s = "iamshadenyeah"
print "S" + s[4:]

t = "a"
# print 't'.find('t')
t.find (t+'!!!')+1
