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
import urllib2
def get_page(url):
    return urllib2.urlopen(url).read()

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

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results

words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()
counts = test_hash_function(hash_string, words, 100)
print counts


    

