#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# recursion.py
# --------------------
# Left part 5. Heading into part 6 which seems as if it may be all about recursion.
# 
#
# @author Shaden, 0x899319D4251502BA
# @date  7 March 2015
# @version 0.0.1
##############################################################################



def factorial(n):                   # hmm, interesting.
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print factorial(0)
print factorial(5)
print factorial(10)

def countdownn(n):                  # brokeass code
    if n != 0:
        return 0
    else:
        countdownn(n - 1)

print countdownn(11)
