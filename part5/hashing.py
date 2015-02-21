#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# hashing.py
# --------------------
# Part 5: learning about hashing, buckets, and modulo?
#
# @author Shaden, 0x899319D4251502BA
# @date 21 February 2015
# @version 0.0.1
##############################################################################


#print ord('a')
#print ord('A')
#print 9 % 25


def hash_string(keyword, buckets):  # this should give us a modulo that
    x = 0                           # will distribute evenly amongst a hash table?
    for e in keyword:
        x = ord(e) + x
    return x % buckets
print hash_string('a', 12) # 1
print hash_string('b', 12) # 2
print hash_string('a', 13) # 6
print hash_string('au', 12) # 10
print hash_string('uberhashed', 12) # 7


    

