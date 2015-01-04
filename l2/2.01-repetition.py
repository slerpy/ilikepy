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
print rest_of_string("oshaden")

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

def bigger(a,b):
    if a>b:
        return a
    else:
        return b
print bigger(3,2)
print (7,3)
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
print is_friend ("Steve")

###
# Now we can be friends with anyone whose names start with D or N! Who's discriminatory now?
##

def is_friend(name):
    if name[0]=="D":
        return True
    if name[0]=="N":
        return True
    else:
        return False
print "Separator"
print is_friend("Geraldine")
print is_friend("Nom Nommer")
print is_friend("Donald McRonald")
#



