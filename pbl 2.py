# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fact(n):
    output = 1
    for term in range(1, n+1):
        output *= term
    return output

def exptaylor(n,x):
    output = 1
    for term in range(1,n+1):
        output += 1/fact(term)*x**term
    return output
