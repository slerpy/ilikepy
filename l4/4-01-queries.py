#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
# 01-quieries.py
# --------------------
# The next chapter in our adventures in python saga. giddyup!
#
# @author Shaden, 0x899319D4251502BA
# @date 13 February 2015
# @version 0.0.1
##############################################################################


#add_to_index,
# takes 3 inputs:
# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []


def add_to_index(index, keyword, url):
    for e in index:
        if e[0] == keyword:
            e[1].append(url)
            return
    index.append([keyword,[url]])


add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'computing', 'http://acm.org')
add_to_index(index, 'udacity', 'http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]

# A procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]


def lookup(index, keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
    return []

print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']
