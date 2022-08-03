# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

def fact(n):
    output = 1
    for term in range(1, n+1):
        output *= term
    return output

def exptaylor(n,x):
    output = 0
    for term in range(0,n+1):
        output += 1/fact(term)*x**term
    return output

def betterexp(n,x):
    output = 1
    term = 1
    for i in range(1,n+1):
        term *= x/i
        output += term
    return output

xinput = np.linspace(-2,1,30)
youtput = betterexp(50,xinput)

plt.plot(xinput,youtput)

