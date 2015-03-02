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


courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253':
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262':
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def is_offered(courses, course, hexamester):        # return True if course is listen in courses during given hexamester
    for c in courses[hexamester]:
        if course in courses[hexamester]:
            return True
        return False


print is_offered(courses, 'cs101', 'apr2012')
#>>> True

print is_offered(courses, 'cs003', 'apr2012')
#>>> False
#print is_offered(courses, 'cs888', 'mar2013')
print is_offered(courses, 'cs001', 'jan2044')
#>>> True


def when_offered(courses,course):           # return the hexamester in which a course in courses is offered.
    are_we_there_yet = []
    for hexa in courses:
        if course in courses[hexa]:
            are_we_there_yet.append(hexa)
    return are_we_there_yet

print when_offered(courses, 'cs101')
print when_offered(courses, 'bio893')
print when_offered(courses, 'cs003')