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
