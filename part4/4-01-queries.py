#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
# 01-queries.py
# --------------------
# The next chapter in our adventures in python saga. giddyup!
#
# @author Shaden, 0x899319D4251502BA
# @date 13 February 2015
# @version 0.0.1
##############################################################################

index = []


def add_to_index(index, keyword, url):  # populate our index, but first make sure keyword is not already in list.
    for e in index:
        if e[0] == keyword:
            e[1].append(url)
            return
    index.append([keyword,[url]])


def lookup(index, keyword):     # lookup keywords in our list.
    for e in index:
        if e[0] == keyword:
            return e[1]
    return []


def add_page_to_index(index,url,content):   # .split all words into a list and run them through the add_to_index
    for words in content.split():           #  procedure to populate our index.
        add_to_index(index, words, url)



add_page_to_index(index,'fake.text',"This is a test")
print index


def split_string(source,splitlist):  # take two inputs, a string to split, and a list of characters as splitpoints.
    output = []
    split = True
    for e in source:
        if e in splitlist:
            split = True
        else:
            if split:
                output.append(e)
                split = False
            else:
                output[-1] = output[-1] + e
    return output


out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']