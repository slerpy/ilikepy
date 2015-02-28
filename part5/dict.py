#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# dict.py
# --------------------
# Moving on through 5th section. Now, rather than using / creating our own hashtables, we're going to use the default function in python.
#
# @author Shaden, 0x899319D4251502BA
# @date 25 February 2015
# @version 0.0.1
##############################################################################

elemental = {
    'hydrogen': 1,
    'helium': 2,
    'carbon': 6
}
elemental['lithium'] = 3
# elemental['nitrogen'] = 8
# elemental['nitrogen'] = 7

print elemental

def lookup(index, keyword):     # new lookup using built in dictionary
    if keyword in index:
        return index[keyword]
    return None