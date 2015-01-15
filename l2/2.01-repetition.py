__author__ = 'shaden'

###
# procedural abstraction
# procedure: inputs ----> procedure --->> outputs
# this is absolutely what i wanted on last url slerping code lol.
###

# s=('<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Udacity</title></head><body><h1>Udacity</h1><p><b>Udacity</b> is a private institution of<a href="http://www.wikipedia.org/wiki/Higher_education">higher education founded by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".</p>  <p> It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Udacity is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="http://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p>     </body></html>')
# def slerp_next_target(s):
#     start_link=s.find("<a href=")
#     start_quote=s.find('"',start_link)
#     end_quote=s.find('"',start_quote+1)
#     url=s[start_quote+1:end_quote]
#     return url,end_quote
# print url

def rest_of_string(s):
    return s[1:]
print rest_of_string ("oshaden")

def square(a):
    a = a * a
    return a
print square (5)


def sum3(a,b,c):
    return a+b+c
print sum3(1,2,3)

###
# doo bee doobedo.
###
def abbaize(firstWord, secondWord):
    return firstWord+secondWord+secondWord+firstWord
print abbaize("shaden","whoa")
print abbaize("oh","whoa")

# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(search,target):
    first=search.find(target)
    two=search.find(target,first+1)

    return two


#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#print find_second(danton, 'audace')
#>>> 25

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
#>>> 13

###
# comparative operators return boolean values
##

def absolute(x):
    if x<0:
        x=-x
    return x

def bigger(a, b):
    if a > b:
        return a
    else:
        return b
print bigger(3, 2)
print (7, 3)
#print (10,6)
#print (5,9)

###
# If first name begins with D, they are a friend, otherwise, fuck them? Weird class lol.
##
def is_friend(name):
    if name[0] == "D":
        return True
    else:
        return False
print is_friend('Dave')
print is_friend('Sherlock')
print is_friend('Watson')

###
# a much shorter version of the above example
##


def is_friend(name):
    return name[0] == "D"
print is_friend("Steve")

###
# Now we can be friends with anyone whose names start with D or N! Who's discriminatory now?
##

def is_friend(name):
    if name[0] == "D":
        return True
    if name[0] == "N":
        return True
    else:
        return False
print "Separator"
print is_friend("Geraldine")
print is_friend("Nom Nommer")
print is_friend("Donald McRonald")
#


###
# using 'or': i teensy weensy cheated and used 'and' rather than 'or'
###

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a,b,c):
    if a>b and a>c:
        return a
    else:
        if b>c:
            return b
        else:
            return c

# print biggest(3, 6, 9)
# >>> 9

# print biggest(6, 9, 3)
# >>> 9

# print biggest(9, 3, 6)
# >>> 9

print biggest(3, 3, 9)
# >>> 9


###
# using the bigger proc from way ^^^ there :D
###
def biggerest(a, b, c):
    return bigger(bigger(a, b), c)
print biggerest(4, 6, 3)

###
# first loop
###

i = 0
while i != 10:
    i = i + 1
    print i


###
# Slerpy, do not uncomment below block. Loops forever. and ever. and ever. and ever. and ever...
###

# i = 1
# while i != 10:
#    i = i + 2
#    print i

# separate

print "----------------"
print "----------------"

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.


def print_numbers(n):
    i = 1
    while i <= n:
        print i
        i = i + 1
print_numbers(5)

#separator
print "-----------"
print "factored"
print "-----------"


# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

###
# I don't feel good about this one. Srsly. Way to much trial and error. Come back and work on this.
###

def factored(n):
    i = 1
    while n >= 1:
        i = i * n
        n = n - 1
    return i
print factored(4)
print factored(8)
print factored(52)
print factored(26)


###
# k mostly finished up with l.2
# just moving to the last lessons. :D :D
###

###
# last of the problem sets.
###

# a procedure that will calculate median using previously used functions.


def median(a, b, c):
    if biggest(a, b, c) == a:
        return bigger(b, c)
    else:
        if biggest(a, b, c) == b:
            return bigger(a, c)
        else:
            if biggest(a, b, c) == c:
                return bigger(a, b)

print(median(1, 2, 3))
print(median(9, 3, 6))
print(median(7, 8, 7))

print "-------------"
print "-------------"

# a procedure that counts down from input int


def countdown(n):
    print n
    while n > 1:
        n = n - 1
        print n
    print "Happy New Year twerps!"

countdown(9)


__author__ = 'shaden'
# a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(string, target):
    first = 0
    last = string.find(target,first)
    while string.find(target, first) != -1:
        last = string.find(target, first)
        first = first + 1
    return last






print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0


print "--------"
print "--------"
# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    fundays = day
    if fundays.find("Saturday") > -1:
        return True
    else:
        if fundays.find("Sunday") > -1:
            return True
        else:
            return False



print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False