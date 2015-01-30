###
# as we move into chapter 3 of our adventures, we appear to be learning how to make
# lists. are these the same as arrays?
###


# procedure to figure out how many days in any chosen month. assumes non leap year

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def how_many_days(month):
    return days_in_month[month - 1]
print how_many_days(11)


# slerping stuff out from lists

countries = [['China', 'Beijing', 1350],
             ['India', 'New Delhi', 1210],
             ['Romania', 'Bucharest', 21],
             ['United States', 'Washington DC', 307]]

print countries[1][1]  # capital of india
print countries[0][2] / countries[2][2]  # multiple of romania pop to china


# mutate stooges to get rid of curly and replace with Shemp

stooges = ['Moe', 'Larry', 'Curly']
stooges[2] = 'Shemp'
print stooges  # ['Moe', 'Larry', 'Shemp']


# takes as its input a list of three numbers, and modifies the value of the third element in the
# input list to be one more than its previous value.
# fixed to be a little more streamlined

spy = [0, 0, 7]


def replace_spy(n):
    n[2] = n[2] + 1
    return n

replace_spy(spy)
print spy  # [0,0,8]


# list append, concatenation, length

p =[1, 2]
p.append(3)
p = p+[4, 5]
print len(p)

p = [1, 2]
q = [3, 4]
p.append(q)

print len(p)


# for loop

def print_all_elements(p):
    for e in p:
        print e

print print_all_elements([1, 3, 4, 5])


# add all ints in a list together

print "sum list"


def sum_list(n):
    result = 0
    for y in n:
        result = result + y
    return result


print sum_list([1, 7, 4])  # 12


# for loop summing how many strings start with U

print "Strings beginning with U"


def measure_u(n):
    result = 0
    for y in n:
        if y[0] == "U":
            result = result +1
    return result
print measure_u(['Umika', 'Umberto'])  # 2
print measure_u(['Utah', 'Tony', 'Unanimous', 'Hillo!', 'Ubfunny'])  # 3


# find first instance of something inside of list
# If there is no matching element,
# return -1.

print "find element"


def find_element(x, y):
    found = 0
    for e in x:
        if e != y:
            found = found + 1
        else:
            return found
    return -1

print find_element([1, 2, 3], 3)  # returns 2
print find_element(['alpha', 'beta'], 'gamma')  # returns -1


# using .index rather than the above

print "find element 2"


def find_element(x, y):
    if y in x:
        return x.index(y)
    else:
        return -1

print find_element([1, 2, 3], 3)  # 2
print find_element(['alpha', 'beta'], 'gamma')  # -1


# take 2 lists, merge them. do not add duplicates

print "Union"


def union(x, y):
    for item in y:
        if item not in x:
            x.append(item)

a = [1, 2, 3]
b = [2, 4, 6]
union(a, b)
print a  # [1,2,3,4,6]
print b  # [2,4,6]

# teh beginning of what may be a long irc script to translate connerspeak to engrish ;)

def connerSpeakFix(x):
    if x == "y'ello":
        end = x[2:]
        all = "h" + end
    return all
print connerSpeakFix("y'ello")


# procedure that will multiply items and return product

print "product"
def product_list(p):
    a = 1
    for e in p:
        a = a * e
    return a
print product_list([9]) # 9
print product_list([1,2,3,4]) # 24
print product_list([]) # 1


# take list and give back largest number or 0 if none

def greatest(p):
    if len(p)==0:
        return 0
    else:
        i=0
        for e in p:
            while e > p[i]:
                i=i+1
        return p[i]

print greatest([4,23,1]) # 23
print greatest([]) # 0


# rewrite of above since simple is probably better

print "greatest redux"
def greatest(list):
    if list == []:
        return 0
    ginormous = list[0]
    for e in list:
        if e > ginormous:
            ginormous = e
    return ginormous
print greatest([4,23,1]) # 23
print greatest([10,68,2,0,25,45,78,99,103,69]) # 103
print greatest([])


# rewrite of above again, because the if statement is needless. i just assign ginormous 0

print "greatest part tree"
def greatest(list):
    ginormous = 0
    for e in list:
        if e > ginormous:
            ginormous = e
    return ginormous
print greatest([3,53,24,52,73,3453,2456,234]) # 3453
print greatest([3,6,8,3,5,9,4]) # 9
print greatest([0])


